class Prompts:
    """Prompts intructions to choose column, row, and number."""

    def __init__(self):
        self.column = ""
        self.row = 0
        self.number = 0

    def input(self):
        "Input from player"
        self.column = "Choose a column (A-I): "
        self.row = input(int("Choose a row (1-9): "))
        self.number = input(
            int("Choose a number to insert in the box (1-9): "))
