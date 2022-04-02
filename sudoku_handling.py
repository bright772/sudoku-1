from sudoku import Sudoku
from text import Prompts
import constants
from sys import exit


class Handling():
    """Handles inserting and removing a number"""

    def __init__(self):
        self.sudoku = Sudoku()
        self.text = Prompts()
        self.game_grid = constants.GAME_GRID

    def num_inserter(self):
        """Inserts a number according to user's input"""
        # print(f"constants.ROW_NUMBERS: {constants.ROW_NUMBERS}")
        # print(f"constants.ROW: {constants.ROW}") #TODO: This only prints 0. self.text.row is the issue.
        row_index = constants.ROW_NUMBERS.index(constants.ROW)
        # print(f"constants.COLUMN_LETTERS: {constants.COLUMN_LETTERS}")
        # print(f"row_index: {row_index}")
        column_index = constants.COLUMN_LETTERS.index(constants.COLUMN)
        # print(f"column_index: {column_index}")
        if constants.GAME_GRID[row_index][column_index] == " ":
            constants.GAME_GRID[row_index].pop(column_index)
            constants.GAME_GRID[row_index].insert(
                column_index, constants.NUMBER)
            # print(constants.NUMBER)

    def num_deleter(self):
        """Deletes a number according to user's input"""
        row_index = constants.ROW_NUMBERS.index(constants.ROW)
        column_index = constants.COLUMN_LETTERS.index(constants.COLUMN)

        if constants.GAME_GRID[row_index][column_index] == constants.GAME_GRID[row_index][column_index]:
            constants.GAME_GRID[row_index].pop(column_index)
            constants.GAME_GRID[row_index].insert(
                column_index, constants.NUMBER)

    def win_checker(self):
        """"Checks when the user wins"""
        for row in constants.GAME_GRID:
            if " " in row:  # Checks each row in the game grid for a space. If it finds one, this function ends.
                return  # the game will continue until the grid is full.

        # compares actual grid with the correct answer grid
        if constants.GAME_GRID == constants.ANSWER_GRID:
            print("YAY! You Won!")
            exit()
