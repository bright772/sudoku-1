from random import randint, Random

class Grids:

    def __init__(self):
        self.answer_grid = []
        self.number = 0

    

    def generate_puzzle_answer(self):
        # Make a matrix, or nested list, that is the answer to the puzzle
        self.answer_grid = [
            [4,7,6,5,3,2,8,1,9],
            [2,5,8,1,4,9,7,3,6],
            [1,9,3,7,6,8,4,2,5],
            [6,4,7,8,2,5,1,9,3],
            [5,1,9,3,7,6,2,8,4],
            [3,8,2,9,1,4,5,6,7],
            [9,2,4,6,8,7,3,5,1],
            [7,6,1,2,5,3,9,4,8],
            [8,3,5,4,9,1,6,7,2],
        ]
    
    def generate_missing_indices(self):
        easy_mode = 36
        missing_indices = []
        for i in easy_mode:
            x = randint(0,8)
            y = int(easy_mode / 4)
            missing_indices.append([x, y])

        print ("Missing Indices: ")
        for i in range(0, easy_mode):
            print(missing_indices[i])
            


    def generate_puzzle(self, grid):
        for i in 36:
            x = randint(0,8)
            y = 0
            puzzle_list = []
            
            
    
   
