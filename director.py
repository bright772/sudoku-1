from action import SelectAction
from action import Action
from sudoku import Sudoku


class Director:

    def __init__(self):
        self.is_playing = True
        self.action = Action()
        self.sudoku = Sudoku()

    def start_game(self):
        print("Welcome to the Sudoku Game!")
        while self.is_playing:
            # displays sudoku grid
            # TODO: display sudoku grid
            self.sudoku
            # displays actions for the user to choose
            self.action.actions()

        self.is_playing = False
