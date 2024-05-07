from rasa_sdk import Action
from rasa_sdk.events import SlotSet, ReminderScheduled, ConversationPaused, ConversationResumed, FollowupAction, Restarted, ReminderScheduled
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class TestAction(Action):

    def name(self):
        return 'test_action'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="hello world")
        dispatcher.utter_message(template="utter_default")
        return []