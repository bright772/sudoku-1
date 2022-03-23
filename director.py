from grids import Grids
from random import randint, Random

class Director:

    def __init__(self):
        self.answer_grid = Grids()
        self.is_playing = True
        self.answer_indices = []

    def start_game(self):
        while self.is_playing:
            self.do_updates()

    def do_updates(self):
        self.answer_grid.generate_puzzle_answer() #builds the 9x9 grid of the completed sudoku puzzle
        
        #This section is where I hope to generate coordinates in the 9x9 answer grid where we will remove numbers, replace them with blank spots, and then that will be the actual game_grid
        #I want this in grids.py but I don't know how to run it here
        easy_mode = 36 #easy mode makes 36 blank spaces in the puzzle
        missing_indices_row = [] #y coordinates list
        missing_indices_column = [] #x coordinates list
        for i in range(easy_mode):
            x = randint(0,8) #x is random 
            y = int(i / 4) #y goes in order from 0-8 taking an equal amount from each row. There's probably a better way
            missing_indices_row.append(y)
            missing_indices_column.append(x)

        #printing the missing indices as a test.
        print ("Missing Indices: ")
        for i in range(len(missing_indices_column)):
            print(f"{missing_indices_row[i]}, {missing_indices_column[i]}")

        self.is_playing = False

