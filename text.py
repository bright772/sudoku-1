class Prompts:
    """Prompts intructions to choose column, row, and number."""

    def __init__(self):
        self.column = ""
        self.row = 0
        self.number = 0

    def input(self):
        "Input from player"
        self.column = input("Choose a column (A-I): ")
        self.row = int(input("Choose a row (1-9): "))
        self.number = int(
            input("Choose a number to insert in the box (1-9): "))
