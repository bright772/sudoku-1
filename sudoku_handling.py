from sudoku import Sudoku
from text import Prompts
import constants

class Handling(Sudoku):
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
        row_index = constants.ROW_NUMBERS.index(self.text.row)
        print(row_index)
        column_index = constants.COLUMN_LETTERS.index(self.text.column)
        print(column_index)
        self.game_grid[row_index].pop(column_index)
        
        self.game_grid[row_index].insert(column_index, self.text.number)
        