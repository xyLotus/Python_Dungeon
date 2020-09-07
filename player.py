"""
Player object for the Python Dungeon game.
"""
import uuid


__author__ = 'bellrise'
__version__ = 0.1


class Player:
    def __init__(self, name, userid):
        self.NAME = name
        self.ID = uuid.uuid4()
        self.INVENTORY = Inventory()



class Inventory:
    pass
