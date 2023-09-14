'''
This file contains the GUI class which represents the graphical user interface of the Connect Four game.
'''
import tkinter as tk
from game import Game
class GUI:
    def __init__(self, game):
        self.game = game
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Connect Four")
        # Create the game board
        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()
        self.buttons = []
        for row in range(6):
            row_buttons = []
            for col in range(7):
                button = tk.Button(self.board_frame, width=5, height=2, command=lambda c=col: self.make_move(c))
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        # Create the status label
        self.status_label = tk.Label(self.window, text="Player 1's turn")
        self.status_label.pack()
    def start(self):
        self.window.mainloop()
    def make_move(self, column):
        if self.game.make_move(column):
            self.update_board()
            winner = self.game.check_winner()
            if winner != 0:
                self.show_winner(winner)
            else:
                self.update_status()
    def update_board(self):
        for row in range(6):
            for col in range(7):
                player = self.game.board[row][col]
                if player == 0:
                    self.buttons[row][col].configure(bg="white")
                elif player == 1:
                    self.buttons[row][col].configure(bg="red")
                elif player == 2:
                    self.buttons[row][col].configure(bg="yellow")
    def update_status(self):
        if self.game.current_player == 1:
            self.status_label.configure(text="Player 1's turn")
        else:
            self.status_label.configure(text="Player 2's turn")
    def show_winner(self, winner):
        if winner == 1:
            self.status_label.configure(text="Player 1 wins!")
        else:
            self.status_label.configure(text="Player 2 wins!")