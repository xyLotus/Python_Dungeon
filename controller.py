"""
Takes the data from main.py and controls the user-system interactions.
"""
import player


class Controller:
    def __init__(self, username, difficulty):
        # Global definitions
        self.difficulty = difficulty

        # Creates a new player
        self.Player = player.Player(username)

        # Starts the game
        self.start()

    def start(self):
        # Adventure time
        print('Adventure time!')

        self.Player.INVENTORY.add('paper', 12)
        self.Player.INVENTORY.add('apple', 3)
