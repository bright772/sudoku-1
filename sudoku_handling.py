from sudoku import Sudoku
from text import Prompts
import constants


class Handling():
    """Handles inserting and removing a number"""

    def __init__(self):
        self.sudoku = Sudoku()
        self.text = Prompts()
        self.game_grid = constants.GAME_GRID

    def num_inserter(self):
        """Inserts a number according to user's input"""
        row_index = constants.ROW_NUMBERS.index(constants.ROW)
        column_index = constants.COLUMN_LETTERS.index(constants.COLUMN)
        if constants.GAME_GRID[row_index][column_index] == " ": #if the list has a space, replace it with the number
            constants.GAME_GRID[row_index].pop(column_index)
            constants.GAME_GRID[row_index].insert(
                column_index, constants.NUMBER)
        else:
            print("You can only insert a number into a blank space.")

    def num_deleter(self):
        """Deletes a number according to user's input"""
        row_index = constants.ROW_NUMBERS.index(constants.ROW)
        column_index = constants.COLUMN_LETTERS.index(constants.COLUMN)

        if constants.GAME_GRID[row_index][column_index] == constants.GAME_GRID[row_index][column_index]:
            constants.GAME_GRID[row_index].pop(column_index)
            constants.GAME_GRID[row_index].insert(
                column_index, constants.NUMBER)

    def win_checker(self, is_playing):
        """Checks when the user wins"""
        for row in constants.GAME_GRID:
            if " " in row:  # Checks each row in the game grid for a space. If it finds one, this function ends.
                return is_playing# the game will continue until the grid is full.

        # compares actual grid with the correct answer grid
        winning = True
        for i in range(len(constants.COLUMN_LETTERS)):
            for j in range(len(constants.COLUMN_LETTERS)):
                if constants.GAME_GRID[i][j] == constants.ANSWER_GRID[i][j] and winning == True:
                    winning = True
                else:
                    winning = False
                
        
        if winning:
            print("Yes! You won the game!")
            is_playing = False
            return is_playing
        else:
            print("You lost the game.")
            is_playing = False
            return is_playing

