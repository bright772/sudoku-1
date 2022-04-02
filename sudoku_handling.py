from sudoku import Sudoku
from text import Prompts
import constants

class Handling():
    """Handles inserting and removing a number"""

    def __init__(self):
        self.sudoku = Sudoku()
        self.text = Prompts()
        self.game_grid = constants.GAME_GRID
        
    # def game_grid_maker(self, grid, difficulty_variable=4):
    #     if self.text.column == self.sudoku.cols and self.text.row == self.sudoku.rows:
    #         game_grid = []
    #         for row in grid:
    #             self.number = self.text.number
    #             row.insert(" ", self.number)
    #         game_grid.append(row)
    #         return super().game_grid_maker(grid, difficulty_variable)

    # def print_board(self, grid, rows=..., cols=...):
    #     return super().print_board(grid, rows, cols)

# NOTE: Im trying to rewrite the code from Sudoku to insert the users's input number


    def num_inserter(self):
        # print(f"constants.ROW_NUMBERS: {constants.ROW_NUMBERS}")
        # print(f"constants.ROW: {constants.ROW}") #TODO: This only prints 0. self.text.row is the issue.
        row_index = constants.ROW_NUMBERS.index(constants.ROW)
        # print(f"constants.COLUMN_LETTERS: {constants.COLUMN_LETTERS}")
        # print(f"row_index: {row_index}")
        column_index = constants.COLUMN_LETTERS.index(constants.COLUMN)
        # print(f"column_index: {column_index}")
        if constants.GAME_GRID[row_index][column_index] == " ":
            constants.GAME_GRID[row_index].pop(column_index)
            constants.GAME_GRID[row_index].insert(column_index, constants.NUMBER)
        else:
            print("You can only insert a number into a blank space.")

    def win_checker(self):
        for row in constants.GAME_GRID: 
            if " " in row: #Checks each row in the game grid for a space. If it finds one, this function ends.
                return #the game will continue until the grid is full.
        
        #TODO: make the win condition. My idea was to compare if GAME_GRID == ANSWER_GRID is a win, anything else resets the game by making GAME_GRID = GAME_GRID_BLANK
        
    
        