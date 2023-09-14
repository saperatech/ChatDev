'''
This is the main file of the Connect Four game.
'''
from game import Game
from gui import GUI
def main():
    # Create a new game instance
    game = Game()
    # Create the GUI and start the game
    gui = GUI(game)
    gui.start()
if __name__ == "__main__":
    main()