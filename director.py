from action import SelectAction
from action import Action
from sudoku import Sudoku
import constants


class Director:

    def __init__(self):
        self.is_playing = True
        self.action = Action()
        self.sudoku = Sudoku()
        constants.GAME_GRID = self.sudoku.game_grid_maker(constants.ANSWER_GRID)

    def start_game(self):
        print("Welcome to the Sudoku Game!")

        while self.is_playing:
            # displays sudoku grid
            # TODO: display sudoku grid
            self.sudoku.print_board(constants.GAME_GRID)
            # displays actions for the user to choose
            self.action.actions()
            #self.do_updates #should this add the chosen number to the chosen position on the board?
            self.action.todo()
            if self.action.instruction == 3:
                break

        self.is_playing = False
