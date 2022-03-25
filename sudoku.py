from random import randint

#Create the answer grid.
is_playing = True
answer_grid = [
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
rows_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
col_list = [1,2,3,4,5,6,7,8,9]

def game_grid_maker(grid, difficulty_variable = 4):
    #This function takes an answer grid and removes a certain amount of variables from each line (difficulty variable)
    game_grid = [] #The grid that the player will see
    for row in grid:        
        removals = randint(difficulty_variable - 1, difficulty_variable + 1) # + or - 1 for the sake of randomness
        for removal in range(0, removals): # how many times it will remove something
            remove = randint(0, 8) #the number 1-9 that will be removed from the row
            row.pop(remove) #remove the number
            row.insert(remove, " ") #insert a space
        game_grid.append(row) #add this row with blank spaces to the game_grid list
    return game_grid #now we have our game grid

def square_chooser(grid, row_letters=rows_list, col_numbers=col_list):
    #user does their inputs. The loop repeats if the inputs are invalid.
    looper = True
    while looper:
        try:
            square_choice = input(F"Enter a letter and number to choose a square (example A1): ")
            num_choice = int(input(f"Enter the number to insert into the selected square: "))
            row_letter = square_choice[0].upper()
            col = int(square_choice[1])
            row = letter_to_number(row_letter)

            if row_letter in row_letters and col in col_list and num_choice in col_numbers and grid[row-1][col-1]==" ":
                #the inputs needs to be a letter followed by a number, then a single number, and finally a blank space on the grid must be chose.
                grid[row-1].pop(col-1)
                grid[row-1].insert(col-1, num_choice)
                looper = False
            else:
                print("Invalid Entry.")
        except:
            print("Invalid Entry!")
        new_list = grid
    return new_list

def letter_to_number(letter, row_letters=rows_list, row_numbers=col_list):
    number = row_numbers[row_letters.index(letter)]
    print(number)
    return number

def print_board(grid, row_letters=rows_list):
    #This function prints the board
    breaker = "    ---+---+---+---+---+---+---+---+---" #print the breaker in between each line of numbers
    column_nums = "     1   2   3   4   5   6   7   8   9"
    lid = "    -----------------------------------"
    
    print(f"{column_nums}\n{lid}")
    i = 0
    for row in (grid):
        print(f"{row_letters[i]}  ", end ="") #print the row letter. the end = "" makes it so there is no line break.
        for j in range(len(row)):
            print(f"| {row[j]} ", end="") #print the numbers in the row
        print(f"\n{breaker}")
        i += 1

def win_checker(grid):
    #the sum of each row, column, and square should be equal to 45
    pass

game_grid = game_grid_maker(answer_grid)

while is_playing:
    print_board(game_grid) #printing the grid for testing purposes.
    square_chooser(game_grid)
    #maybe when grid is full the game stops?
    