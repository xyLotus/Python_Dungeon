"""
Takes the data from main.py and controls the user-system interactions.
"""
import player
import event


class Controller:
    def __init__(self, username, difficulty):
        """
        This is called when main.py finishes the setup.
        The Player and EventHandler instance is created here
        for use in main().
        """
        self.difficulty = difficulty

        # Creates a new player
        self.Player = player.Player(username)
        self.Event = event.EventHandler(username)

        # Starts the game
        self.main()

    def main(self):
        """
        This is the main method called when the program starts
        place all game functionality here, external classes and
        methods can be used.
        """
        print('\n\nAdventure time!')

        # Game

        self.Player.INVENTORY.add('coin', 250)

        print(self.Player.INVENTORY)
