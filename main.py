import controller

# Global definitions
version = '0.0.1'


class Main:
    # This is responsible for taking data from the user, like
    # username and difficulty
    def __init__(self):
        self.username = input('\nYour name: ')
        self.difficulty = None

        print('\nSelect your difficulty: 1 - easy, 2 - normal, 3 - hard')
        while self._validator(self.difficulty) is False:
            self.difficulty = input('Difficulty: ')
        self._difficulty()

        controller.Controller(self.username, self.difficulty)

    @staticmethod
    def _validator(d):
        """ Checks if the difficulty is valid """
        if d == '1' or d == '2' or d == '3':
            return True
        else:
            return False

    def _difficulty(self):
        """ Formats the difficulty setting into a string """
        i = self.difficulty
        if i == '1':
            out = 'Easy'
        elif i == '2':
            out = 'Normal'
        else:
            out = 'Hard'
        self.difficulty = out

    @property
    def userdata(self):
        """ Used for reading userdata """
        return 'Username @ ' + self.username, \
               'Difficulty @ ' + self.difficulty


# The actual game
print('Welcome to the Python Dungeon! ' + version)
main = Main()

input('\n\n\n[Press ENTER to exit]')

# So many people don't like cheese. Do you actually like cheese?
# I actually do as a matter of fact.
