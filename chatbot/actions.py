# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import math

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

in_session = False


class ActionSkillsBreakdown(Action):

    def name(self) -> Text:
        return "action_skills_breakdown"

    def run(self, dispatcher, tracker, domain):
        global in_session
        in_session = False

        eps = tracker.current_slot_values()
        eps.pop('name', None)
        eps.pop('location', None)

        skill_values = ['Very Low', 'Low', 'Medium', 'High', 'Very High', 'Excellent']

        ordered_skills = [f"{key}: Skill Value = {value}" for key, value in sorted(eps.items(), key=lambda item: item[1])]
        ordered_skills = '\n\n'.join(ordered_skills)

        dispatcher.utter_message(f"EP1.1 - Interaction: Skill Level = {skill_values[math.floor(eps.get('EP1_1'))]}\n\n"
                                 f"EP1.2 - Initiation: Skill Level = {skill_values[math.floor(eps.get('EP1_2'))]}\n\n"
                                 f"EP2.1 - Hello: Skill Level = {skill_values[math.floor(eps.get('EP2_1'))]}\n\n"
                                 f"Skills worst to best: \n\n{ordered_skills}")

        return []


class ActionUtterGreet(Action):

    def name(self) -> Text:
        return "action_utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global in_session
        in_session = True

        name = tracker.get_slot("name")

        if name is not None:
            dispatcher.utter_message(f'Hi {name}!')
        else:
            dispatcher.utter_message('Hi!')

        ep2_1 = tracker.get_slot("EP2_1")
        if tracker.latest_message['intent'].get('name') != 'no_initiation':
            if ep2_1 < 5:
                ep2_1 += 1
        else:
            if ep2_1 > 5:
                ep2_1 -= 0.5

        return [SlotSet("EP2_1", ep2_1)]


class ActionGoodbye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher, tracker, domain):

        global in_session
        in_session = False

        dispatcher.utter_message('Goodbye!')

        return []


class ActionUtterUserName(Action):

    def name(self) -> Text:
        return "action_utter_user_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")

        if name is not None:
            dispatcher.utter_message(f'Your name is {name}')
        else:
            dispatcher.utter_message("I'm afraid I don't know your name. What is it?")

        return []


class ActionUtterGoodToMeetYou(Action):

    def name(self) -> Text:
        return "action_utter_goodtomeetyou"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")

        if name is not None:
            dispatcher.utter_message(f"It's a pleasure to meet you {name}!")
        else:
            dispatcher.utter_message("It's lovely to meet you!")

        return []


class ActionAskWhatIsYourName(Action):

    def name(self) -> Text:
        return "action_ask_whatisyourname"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")

        if name is None:
            dispatcher.utter_message("What is your name?")
        else:
            dispatcher.utter_message(f"It's great to talk to you {name}!")

        return []


class ActionInteraction(Action):
    """User interaction so increase EP1_1 value"""
    def name(self) -> Text:
        return "action_interaction"

    def run(self, dispatcher, tracker, domain):
        global in_session
        in_session = True

        ep1_1 = tracker.get_slot("EP1_1")

        if ep1_1 < 5:
            ep1_1 += 0.5

        return [SlotSet("EP1_1", ep1_1)]


class ActionNoInteraction(Action):
    """No user interaction so decrease EP1_1 value"""

    def name(self) -> Text:
        return "action_no_interaction"

    def run(self, dispatcher, tracker, domain):
        ep1_1 = tracker.get_slot("EP1_1")

        if in_session:
            if ep1_1 > 0:
                ep1_1 -= 1

        return [SlotSet("EP1_1", ep1_1)]


class ActionSlowInteraction(Action):
    """User interaction slow so decrease EP1_1 value towards the middle (3)"""

    def name(self) -> Text:
        return "action_slow_interaction"

    def run(self, dispatcher, tracker, domain):
        ep1_1 = tracker.get_slot("EP1_1")

        if in_session:

            if ep1_1 > 3:
                ep1_1 -= 1

        return [SlotSet("EP1_1", ep1_1)]


class ActionInitiation(Action):
    """User initiated conversation so increase EP1_2 value"""

    def name(self) -> Text:
        return "action_initiation"

    def run(self, dispatcher, tracker, domain):
        ep1_2 = tracker.get_slot("EP1_2")

        if ep1_2 < 5:
            ep1_2 += 1

        return [SlotSet("EP1_2", ep1_2)]


class ActionNoInitiation(Action):
    """User did not initiate conversation so decrease EP1_2 value"""

    def name(self) -> Text:
        return "action_no_initiation"

    def run(self, dispatcher, tracker, domain):
        ep1_2 = tracker.get_slot("EP1_2")

        if ep1_2 > 1:
            ep1_2 -= 2
        elif ep1_2 > 0:
            ep1_2 -= 1

        return [SlotSet("EP1_2", ep1_2)]
