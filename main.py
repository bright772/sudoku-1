from director import Director

director = Director()
director.start_game()

from random import randint

class GameBoard:
    def __init__(self, row1, row2, row3, row4, row5, row6, row7, row8, row9):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        self.row4 = row4
        self.row5 = row5
        self.row6 = row6
        self.row7 = row7
        self.row8 = row8
        self.row9 = row9

    
    def RemoveNumbers(self):
        pass

    def ChangeBoard(self, rowChoice, columnChoice, numberChoice):
        # Create Actual Row Name
        selectedRow = "row" + rowChoice

        # Create Actual Row Index
        if columnChoice == "A":
            selectedColumn = 0
        if columnChoice == "B":
            selectedColumn = 1
        if columnChoice == "C":
            selectedColumn = 2
        if columnChoice == "D":
            selectedColumn = 3
        if columnChoice == "E":
            selectedColumn = 4
        if columnChoice == "F":
            selectedColumn = 5
        if columnChoice == "G":
            selectedColumn = 6
        if columnChoice == "H":
            selectedColumn = 7
        if columnChoice == "I":
            selectedColumn = 8

        # Insert Player's Number
        self.selectedRow[selectedColumn] = numberChoice
    
    def DisplayBoard(self):
        print("|A--B--C-|D--E--F-|G--H--I-|")
        print(gameBoard.row1)
        print("|        |        |         |")
        print(gameBoard.row2)
        print("|        |        |         |")
        print(gameBoard.row3)
        print("|________|________|_________|")
        print(gameBoard.row4)
        print("|        |        |         |")
        print(gameBoard.row5)
        print("|        |        |         |")
        print(gameBoard.row6)
        print("|________|________|_________|")
        print(gameBoard.row7)
        print("|        |        |         |")
        print(gameBoard.row8)
        print("|        |        |         |")
        print(gameBoard.row9)
        print("|________|________|_________|")

# Generate Full Game Board
gameBoard = GameBoard([4, 7, 6, 5, 3, 2, 8, 1, 9],
                      [2, 5, 8, 1, 4, 9, 7, 3, 6],
                      [1, 9, 3, 7, 6, 8, 4, 2, 5],
                      [6, 4, 7, 8, 2, 5, 1, 9, 3],
                      [5, 1, 9, 3, 7, 6, 2, 8, 4],
                      [3, 8, 2, 9, 1, 4, 5, 6, 7],
                      [9, 2, 4, 6, 8, 7, 3, 5, 1],
                      [7, 6, 1, 2, 5, 3, 9, 4, 8],
                      [8, 3, 5, 4, 9, 1, 6, 7, 2])

# Remove Random Number From Each Row
removedIndex1 = gameBoard.row1[randint(0, 8)]
gameBoard.row1[removedIndex1] = " "
removedIndex2 = gameBoard.row2[randint(0, 8)]
gameBoard.row2[removedIndex2] = " "
removedIndex3 = gameBoard.row3[randint(0, 8)]
gameBoard.row3[removedIndex3] = " "
removedIndex4 = gameBoard.row4[randint(0, 8)]
gameBoard.row4[removedIndex4] = " "
removedIndex5 = gameBoard.row5[randint(0, 8)]
gameBoard.row5[removedIndex5] = " "
removedIndex6 = gameBoard.row6[randint(0, 8)]
gameBoard.row6[removedIndex6] = " "
removedIndex7 = gameBoard.row7[randint(0, 8)]
gameBoard.row7[removedIndex7] = " "
removedIndex8 = gameBoard.row8[randint(0, 8)]
gameBoard.row8[removedIndex8] = " "
removedIndex9 = gameBoard.row9[randint(0, 8)]
gameBoard.row9[removedIndex9] = " "

# Display Initial Game Board
gameBoard.DisplayBoard()

# Ask For User Input
rowChoice = input("Please choose a row. (Enter 1-9) ")
columnChoice = input("Please choose a column. (Enter A, B, C, D, E, F, G, H, I) ")
selectedNumber = input("Please choose a number. (Enter 1-9) ")

# Change Game Board
gameBoard.ChangeBoard(rowChoice, columnChoice, selectedNumber)

# Display Game Board With Changes
gameBoard.DisplayBoard()
