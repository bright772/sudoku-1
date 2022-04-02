from random import randint
import constants


class Sudoku:
    """Creates and displays the sudoku board"""

    def game_grid_maker(self, grid, difficulty_variable=3):
        """Takes an answer grid and removes a certain amount of variables from each line (difficulty variable)"""
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

    def print_board(self, grid, rows=constants.ROW_NUMBERS, cols=constants.COLUMN_LETTERS):
        """Prints the board"""
        # print the breakers and spacers in between each number and line of numbers
        breaker = "  ⋕---+---+---⋕---+---+---⋕---+---+---⋕"  # ʜ⋕
        breaker_thick = "  ⋕===+===+===⋕===+===+===⋕===+===+===⋕"
        spacers = [" ", " | ", " | ", " ‖ ",
                   " | ", " | ",  " ‖ ", " | ",  " | "]
        counter = 0
        print(" ", end="")
        for i in range(len(cols)):
            print(f"   {cols[i]}", end="")
        print(f"\n{breaker_thick}")
        for row in (grid):
            # print the first number in the row. the end = "" makes it so there is no line break.
            print(f"{rows[counter]} ‖", end="")
            for j in range(len(row)):
                # print the rest of the numbers in the row
                print(f"{spacers[j]}{row[j]}", end="")
            print(" ‖")
            if counter == 2 or counter == 5 or counter == 8:
                print(f"{breaker_thick}")
            else:
                print(f"{breaker}")
            counter += 1
    # printing the grid for testing purposes.
    # print_board(game_grid_maker(constants.ANSWER_GRID))
