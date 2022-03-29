from sudoku import Sudoku
from text import Prompts


class Handling(Sudoku):
    """Handles inserting and removing a number"""

    def __init__(self):
        self.sudoku = Sudoku()
        self.text = Prompts()

    def game_grid_maker(self, grid, difficulty_variable=4):
        if self.text.column == self.sudoku.cols and self.text.row == self.sudoku.rows:
            game_grid = []
            for row in grid:
                self.number = self.text.number
                row.insert(" ", self.number)
            game_grid.append(row)
            return super().game_grid_maker(grid, difficulty_variable)

    def print_board(self, grid, rows=..., cols=...):
        return super().print_board(grid, rows, cols)

# NOTE: Im trying to rewrite the code from Sudoku to insert the users's input number
