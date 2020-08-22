# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import math
import re

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

in_session = False
first_interaction = True
question_asked = False
question_answered = False


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
                                 f"EP2.2 - Name Giving: Skill Level = {skill_values[math.floor(eps.get('EP2_2'))]}\n\n"
                                 f"EP3.1 - Question Asking: Skill Level = {skill_values[math.floor(eps.get('EP3_1'))]}\n\n"
                                 f"EP3.3 - Question Answering: Skill Level = {skill_values[math.floor(eps.get('EP3_3'))]}\n\n"
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
            dispatcher.utter_message(template="utter_greet")

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

        dispatcher.utter_message(template="utter_goodbye")

        # decrease EP3.1 if no questions asked in conversation then reset question_asked
        ep3_1 = tracker.get_slot("EP3_1")

        global question_asked
        if not question_asked:
            if ep3_1 > 0.5:
                ep3_1 -= 1
            elif ep3_1 > 0:
                ep3_1 -= 0.5

        question_asked = False

        # decrease EP3.3 if no questions are answered in the conversation, then reset question_answered
        ep3_3 = tracker.get_slot("EP3_3")

        global question_answered
        if not question_answered:
            if ep3_3 > 1.5:
                ep3_3 -= 2
            elif ep3_3 > 0:
                ep3_3 -= 0.5

        question_answered = False

        # decrease EP2.2 if name hasn't been given in the first interaction
        ep2_2 = tracker.get_slot("EP2_2")

        global first_interaction
        if first_interaction:
            name = tracker.get_slot("name")
            if name is None:
                ep2_2 = 0.0
            else:
                ep2_2 = 5.0

        first_interaction = False

        return [SlotSet("EP3_1", ep3_1), SlotSet("EP3_3", ep3_3), SlotSet("EP2_2", ep2_2)]


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

        ep3_3 = tracker.get_slot("EP3_3")

        if re.search("[?]", tracker.get_last_event_for('bot')['text']) is not None:
            if ep3_3 > 0:
                ep3_3 -= 0.5

        return [SlotSet("EP1_1", ep1_1), SlotSet("EP3_3", ep3_3)]


class ActionSlowInteraction(Action):
    """User interaction slow so decrease EP1_1 value towards the middle (3)"""

    def name(self) -> Text:
        return "action_slow_interaction"

    def run(self, dispatcher, tracker, domain):
        ep1_1 = tracker.get_slot("EP1_1")

        if in_session:

            if ep1_1 > 3.5:
                ep1_1 -= 1
            elif ep1_1 > 3:
                ep1_1 -= 0.5

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


class ActionAnswerWhatIsMyName(Action):

    def name(self) -> Text:
        return "action_answer_whatismyname"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")

        if name is not None:
            dispatcher.utter_message(f'Your name is {name}')
        else:
            dispatcher.utter_message("I'm afraid I don't know your name. What is it?")

        global question_asked
        question_asked = True

        ep3_1 = tracker.get_slot("EP3_1")

        if ep3_1 < 5:
            ep3_1 += 0.5

        return [SlotSet("EP3_1", ep3_1)]


class ActionAnswerHowDoing(Action):

    def name(self) -> Text:
        return "action_answer_howdoing"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_answer_howdoing")

        global question_asked
        question_asked = True

        ep3_1 = tracker.get_slot("EP3_1")

        if ep3_1 < 5:
            ep3_1 += 0.5

        # if the users message included an answer to the bot previously asking howdoing, increase EP3.3
        ep3_3 = tracker.get_slot("EP3_3")
        if re.search("ok|good|great", tracker.get_last_event_for('user')['text']) is not None:
            if ep3_3 < 4.5:
                ep3_3 += 1
            elif ep3_3 < 5:
                ep3_3 += 0.5

            global question_answered
            question_answered = True

        return [SlotSet("EP3_1", ep3_1), SlotSet("EP3_3", ep3_3)]


class ActionAnswerWhatIsPossible(Action):

    def name(self) -> Text:
        return "action_answer_whatispossible"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_answer_whatispossible")

        global question_asked
        question_asked = True

        ep3_1 = tracker.get_slot("EP3_1")

        if ep3_1 < 5:
            ep3_1 += 0.5

        return [SlotSet("EP3_1", ep3_1)]


class ActionAnswerWhatIsYourName(Action):

    def name(self) -> Text:
        return "action_answer_whatisyourname"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_answer_whatisyourname")

        global question_asked
        question_asked = True

        ep3_1 = tracker.get_slot("EP3_1")

        if ep3_1 < 5:
            ep3_1 += 0.5

        return [SlotSet("EP3_1", ep3_1)]


class ActionAnswerWhereFrom(Action):

    def name(self) -> Text:
        return "action_answer_wherefrom"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_answer_wherefrom")

        global question_asked
        question_asked = True

        ep3_1 = tracker.get_slot("EP3_1")

        if ep3_1 < 5:
            ep3_1 += 0.5

        return [SlotSet("EP3_1", ep3_1)]


class ActionAnswerWhereIsThat(Action):

    def name(self) -> Text:
        return "action_answer_whereisthat"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_answer_whereisthat")

        global question_asked
        question_asked = True

        ep3_1 = tracker.get_slot("EP3_1")

        if ep3_1 < 5:
            ep3_1 += 0.5

        return [SlotSet("EP3_1", ep3_1)]


class ActionAnswerWhoAmI(Action):

    def name(self) -> Text:
        return "action_answer_whoami"

    def run(self, dispatcher, tracker, domain):

        name = tracker.get_slot("name")
        location = tracker.get_slot("location")

        if name is None:
            dispatcher.utter_message("I'm afraid I don't know your name. What is it?")
        elif location is None:
            dispatcher.utter_message("I'm afraid I don't know enough about you to answer that question")
            dispatcher.utter_message(template="utter_ask_wherefrom")
        else:
            dispatcher.utter_message(f"You are {name} from {location}")

        global question_asked
        question_asked = True

        ep3_1 = tracker.get_slot("EP3_1")

        if ep3_1 < 5:
            ep3_1 += 0.5

        return [SlotSet("EP3_1", ep3_1)]


class ActionAnswerExplain(Action):

    def name(self) -> Text:
        return "action_answer_explain"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_answer_explain")

        global question_asked
        question_asked = True

        ep3_1 = tracker.get_slot("EP3_1")

        if ep3_1 < 5:
            ep3_1 += 0.5

        ep3_3 = tracker.get_slot("EP3_3")

        if re.search("[?]", tracker.get_last_event_for('bot')['text']) is not None:
            if ep3_3 < 5:
                ep3_3 += 0.5

        return [SlotSet("EP3_1", ep3_1), SlotSet("EP3_3", ep3_3)]


class ActionAnswerBotChallenge(Action):

    def name(self) -> Text:
        return "action_answer_bot_challenge"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_chatbot")

        global question_asked
        question_asked = True

        ep3_1 = tracker.get_slot("EP3_1")

        if ep3_1 < 5:
            ep3_1 += 0.5

        return [SlotSet("EP3_1", ep3_1)]


class ActionUserMoodGreat(Action):

    def name(self) -> Text:
        return "action_user_mood_great"

    def run(self, dispatcher, tracker, domain):
        ep3_3 = tracker.get_slot("EP3_3")

        if tracker.get_last_event_for('bot')['text'] in ['How are you?', 'How are you today?', 'How are you doing?']:
            if ep3_3 < 4.5:
                ep3_3 += 1.0
            elif ep3_3 < 5:
                ep3_3 += 0.5

            global question_answered
            question_answered = True

        dispatcher.utter_message(template="utter_happy")

        return [SlotSet("EP3_3", ep3_3)]


class ActionUserMoodUnhappy(Action):

    def name(self) -> Text:
        return "action_user_mood_unhappy"

    def run(self, dispatcher, tracker, domain):
        ep3_3 = tracker.get_slot("EP3_3")

        if tracker.get_last_event_for('bot')['text'] in ['How are you?', 'How are you today?', 'How are you doing?']:
            if ep3_3 < 4.5:
                ep3_3 += 1.0
            elif ep3_3 < 5:
                ep3_3 += 0.5

            global question_answered
            question_answered = True

        dispatcher.utter_message(template="utter_cheer_up")

        return [SlotSet("EP3_3", ep3_3)]


class ActionUserAffirm(Action):

    def name(self) -> Text:
        return "action_user_affirm"

    def run(self, dispatcher, tracker, domain):
        ep3_3 = tracker.get_slot("EP3_3")

        if re.search("[?]", tracker.get_last_event_for('bot')['text']) is not None:
            if ep3_3 < 4.5:
                ep3_3 += 1.0
            elif ep3_3 < 5:
                ep3_3 += 0.5

            global question_answered
            question_answered = True

        dispatcher.utter_message(template="utter_happy")

        return [SlotSet("EP3_3", ep3_3)]


class ActionUserDeny(Action):

    def name(self) -> Text:
        return "action_user_deny"

    def run(self, dispatcher, tracker, domain):
        ep3_3 = tracker.get_slot("EP3_3")

        if re.search("[?]", tracker.get_last_event_for('bot')['text']) is not None:
            if ep3_3 < 4.5:
                ep3_3 += 1.0
            elif ep3_3 < 5:
                ep3_3 += 0.5

            global question_answered
            question_answered = True

        dispatcher.utter_message(template="utter_sorry_no_help")

        return [SlotSet("EP3_3", ep3_3)]


class ActionUserReactPositive(Action):

    def name(self) -> Text:
        return "action_user_react_positive"

    def run(self, dispatcher, tracker, domain):
        ep3_3 = tracker.get_slot("EP3_3")

        if re.search("[?]", tracker.get_last_event_for('bot')['text']) is not None:
            if ep3_3 < 4.5:
                ep3_3 += 1.0
            elif ep3_3 < 5:
                ep3_3 += 0.5

            global question_answered
            question_answered = True

        return [SlotSet("EP3_3", ep3_3)]


class ActionUserReactNegative(Action):

    def name(self) -> Text:
        return "action_user_react_negative"

    def run(self, dispatcher, tracker, domain):
        ep3_3 = tracker.get_slot("EP3_3")

        if re.search("[?]", tracker.get_last_event_for('bot')['text']) is not None:
            if ep3_3 < 4.5:
                ep3_3 += 1.0
            elif ep3_3 < 5:
                ep3_3 += 0.5

            global question_answered
            question_answered = True

        return [SlotSet("EP3_3", ep3_3)]


class ActionUserInform(Action):

    def name(self) -> Text:
        return "action_user_inform"

    def run(self, dispatcher, tracker, domain):
        ep3_3 = tracker.get_slot("EP3_3")

        if re.search("[?]", tracker.get_last_event_for('bot')['text']) is not None:
            if ep3_3 < 4.5:
                ep3_3 += 1.0
            elif ep3_3 < 5:
                ep3_3 += 0.5

            global question_answered
            question_answered = True

        return [SlotSet("EP3_3", ep3_3)]
