import player
import event

# Global definitions
version = '0.0.1'


class Main:
    """
    Main class with all the functionality
    """
    def __init__(self):
        """
        User name and difficulty selection. Creates the Player
        and EventHandler instance.
        """
        # self.username = input('\nYour name: ')
        self.username = 'TESTING_ACCOUNT'
        # Creates a new player
        self.Player = player.Player(self.username, False)
        self.Event = event.EventHandler(self.username)

        # Starts the game
        self.main()

    def main(self):
        """
        This is the main method called when the program starts.
        Place all game functionality here, external classes and
        methods can be used.
        """
        print('Welcome to the Python Dungeon! ' + version)

        # Game

        self.Player.INVENTORY.new('assad', 3)


# Game initialization and screen hold
run = Main()
input()

# So many people don't like cheese. Do you actually like cheese?
# I actually do as a matter of fact.
