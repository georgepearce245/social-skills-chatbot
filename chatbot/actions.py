# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionUtterGreet(Action):

    def name(self) -> Text:
        return "action_utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")

        if name is not None:
            dispatcher.utter_message(f'Hi {name}!')
        else:
            dispatcher.utter_message('Hi!')

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
