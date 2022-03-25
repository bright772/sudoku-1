from random import randint


class Sudoku:
    # Create the answer grid.
    answer_grid = [
        [4, 7, 6, 5, 3, 2, 8, 1, 9],
        [2, 5, 8, 1, 4, 9, 7, 3, 6],
        [1, 9, 3, 7, 6, 8, 4, 2, 5],
        [6, 4, 7, 8, 2, 5, 1, 9, 3],
        [5, 1, 9, 3, 7, 6, 2, 8, 4],
        [3, 8, 2, 9, 1, 4, 5, 6, 7],
        [9, 2, 4, 6, 8, 7, 3, 5, 1],
        [7, 6, 1, 2, 5, 3, 9, 4, 8],
        [8, 3, 5, 4, 9, 1, 6, 7, 2],
    ]

    def game_grid_maker(grid, difficulty_variable=4):
        # This function takes an answer grid and removes a certain amount of variables from each line (difficulty variable)
        game_grid = []  # The grid that the player will see
        for row in grid:
            # + or - 1 for the sake of randomness
            removals = randint(difficulty_variable-1, difficulty_variable+1)
            # how many times it will remove something
            for removal in range(0, removals):
                # the number 1-9 that will be removed from the row
                remove = randint(0, 8)
                row.pop(remove)  # remove the number
                row.insert(remove, " ")  # insert a space
            # add this row with blank spaces to the game_grid list
            game_grid.append(row)
        return game_grid  # now we have our game grid

    def print_board(grid):
        # This function prints the board
        # print the breaker in between each line of numbers
        breaker = "---+---+---+---+---+---+---+---+---"
        for row in (grid):
            # print the first number in the row. the end = "" makes it so there is no line break.
            print(f" {row[0]} ", end="")
            for j in range(len(row) - 1):
                # print the rest of the numbers in the row
                print(f"| {row[j+1]} ", end="")
            print(f"\n{breaker}")

    # printing the grid for testing purposes.
    print_board(game_grid_maker(answer_grid))
