'''
This file contains the Game class which represents the Connect Four game logic.
'''
class Game:
    def __init__(self):
        # Initialize the game board
        self.board = [[0] * 7 for _ in range(6)]
        self.current_player = 1
    def make_move(self, column):
        # Check if the column is valid
        if column < 0 or column >= 7:
            return False
        # Check if the column is full
        if self.board[0][column] != 0:
            return False
        # Find the lowest empty row in the column
        row = 5
        while row >= 0 and self.board[row][column] != 0:
            row -= 1
        # Make the move
        self.board[row][column] = self.current_player
        # Switch to the next player
        self.current_player = 3 - self.current_player
        return True
    def check_winner(self):
        # Check rows
        for row in range(6):
            for col in range(4):
                if self.board[row][col] != 0 and self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                    return self.board[row][col]
        # Check columns
        for col in range(7):
            for row in range(3):
                if self.board[row][col] != 0 and self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
                    return self.board[row][col]
        # Check diagonals (top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if self.board[row][col] != 0 and self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3]:
                    return self.board[row][col]
        # Check diagonals (top-right to bottom-left)
        for row in range(3):
            for col in range(3, 7):
                if self.board[row][col] != 0 and self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3]:
                    return self.board[row][col]
        # No winner
        return 0