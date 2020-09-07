"""
Core script for the Python Dungeon game, controls
the starting menu and wraps all the functionality.

"""
import os

__author__  = "xyLotus, bellrise"
__version__ = 0.1



class Main:
    """ Main class, responsible for all functionality.
    Calls multiple other classes within. """
    def __init__(self, root):
        self.DATA = dict()
        self.DATA['root'] = root


    def run(self):
        """ Runs the menu """
        with open("banner.txt", "r") as f:
            print(f.read())

    def help(self):
        """ Fallback from a unknown option """
        print('you dumb fuck')


# 

# well thats too bad.txt \o/
# mind sending that to github?

if __name__ == '__main__':
    game = Main(os.getcwd())
    game.run()
