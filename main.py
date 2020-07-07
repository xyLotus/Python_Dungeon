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
        self.Player = player.Player(self.username)
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

        self.Player.INVENTORY.new('apple', 12)
        apple_uuid = self.Player.INVENTORY.lastuuid
        self.Player.INVENTORY.new('paper', 3)
        self.Player.INVENTORY.add(apple_uuid, 123)


        apple_item = self.Player.INVENTORY.uget(apple_uuid)
        print(apple_item.NAME, '->', apple_item.AMOUNT)


# Game initialization and screen hold
run = Main()
input()

# So many people don't like cheese. Do you actually like cheese?
# I actually do as a matter of fact.
