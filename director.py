from action import Action
from sudoku import Sudoku
from sudoku_handling import Handling
import constants


class Director:
    """Plays the game"""

    def __init__(self):
        self.is_playing = True
        self.action = Action()
        self.sudoku = Sudoku()
        self.handling = Handling()
        constants.GAME_GRID = self.sudoku.game_grid_maker(
            constants.ANSWER_GRID)
        constants.GAME_GRID_BLANK = constants.GAME_GRID

    def start_game(self):
        """Starts the game"""
        print("Welcome to the Sudoku Game!")

        while self.is_playing:
            # displays sudoku grid
            self.sudoku.print_board(constants.GAME_GRID)
            # displays actions for the user to choose
            self.action.actions()
            self.action.todo()
            if self.action.instruction == 3:
                break
            # print(f"constants.ROW: {constants.ROW}")
            self.handling.num_inserter()
            self.handling.num_deleter()
            self.handling.win_checker()

        self.is_playing = False
