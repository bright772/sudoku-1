# Sudoku

pop up window - pigame/tkinter/arcade
9x9 grid
mouse to select box, then keyboard to enter number
the game continues until they are correct
difficulties? easy can start with 60% of the puzzle filled in, for example; hard would be 40%
numbers are text

*first we are going to see if we can get it to work in the command line, then a popup window
We can assign column numbers and row letters. A user could type where they want to enter a number eg. B3 and then type a number to fill that space.

Can start by having one puzzle pregenerated, maybe a few puzzles to choose from

classes - Number, Row, Column, Square

box - holds a single number
square - 3x3 grid, holds a number 1-9
grid - the full 9x9 grid of the game (9 squares)
row - 9 boxes side to side
column - 9 boxes top to bottom
