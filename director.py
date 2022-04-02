from action import Action
from sudoku import Sudoku
from sudoku_handling import Handling
from text import Prompts
import constants


class Director:

    def __init__(self):
        self.is_playing = True
        self.action = Action()
        self.sudoku = Sudoku()
        self.handling = Handling()
        self.text = Prompts()
        constants.GAME_GRID = self.sudoku.game_grid_maker(constants.ANSWER_GRID)
        constants.GAME_GRID_BLANK = constants.GAME_GRID

    def start_game(self):
        print("Welcome to the Sudoku Game!")

        while self.is_playing:
            # displays sudoku grid
            self.sudoku.print_board(constants.GAME_GRID)
            # displays actions for the user to choose
            self.action.actions()
            # self.do_updates #should this add the chosen number to the chosen position on the board?
            self.action.todo()
            if self.action.instruction == 3:
                break
            # print(f"constants.ROW: {constants.ROW}") 
            self.handling.num_inserter() 
            self.handling.win_checker()

        self.is_playing = False
