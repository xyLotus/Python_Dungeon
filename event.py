"""
Event Definitions
"""
import random


class EventHandler:
    """
    EventHandler class, creates interactions with the user
    by passing data to it. Should return some kind of a data
    format for the main() method to use.
    """
    def __init__(self, username):
        self.user = username

    def view(self):
        """ Example event, prints a random message from the msgs list """
        msgs = [self.user + ' looks around seeing a beautiful view',
                self.user + ' stands on a hill astonished at the surrounding nature']

        print(msgs[random.choice([0, 1])])
