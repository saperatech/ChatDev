# Connect Four Game User Manual

## Introduction

Welcome to the Connect Four game! This user manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to play the game.

## Installation

To install the Connect Four game, please follow the steps below:

1. Make sure you have Python installed on your computer. If not, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download the Connect Four game files from the provided source.

3. Open a terminal or command prompt and navigate to the directory where you downloaded the game files.

4. Install the required dependencies by running the following command:

   ```
   pip install tkinter
   ```

   This will install the Tkinter library, which is used for the graphical user interface of the game.

5. Once the dependencies are installed, you are ready to play the Connect Four game!

## Main Functions

The Connect Four game provides the following main functions:

1. Start a New Game: Click on the game board to make a move and try to connect four of your pieces in a row, column, or diagonal.

2. Switch Players: The game automatically switches between Player 1 and Player 2 after each move.

3. Check Winner: The game checks for a winner after each move. If a player connects four pieces, the game declares that player as the winner.

4. Display Status: The game displays the current player's turn and the winner's status.

## How to Play

To play the Connect Four game, follow these steps:

1. Run the `main.py` file using Python:

   ```
   python main.py
   ```

   This will start the game and open a graphical user interface window.

2. The game board consists of a 6x7 grid. Each cell represents a position where you can make a move.

3. To make a move, click on any column in the game board. The game will place your piece in the lowest available row of that column.

4. The game will automatically switch to the next player after each move.

5. Keep making moves until one player connects four pieces in a row, column, or diagonal.

6. If a player wins, the game will display a message indicating the winner. If there is no winner and the game board is full, it will display a message indicating a tie.

7. To start a new game, close the game window and run the `main.py` file again.

## Conclusion

Congratulations! You have successfully installed the Connect Four game and learned how to play it. Enjoy the game and have fun connecting four pieces!