import constants


class Prompts:
    """Prompts intructions to choose column, row, and number."""

    def __init__(self):
        self.column = ""
        self.row = 0
        self.number = 0

    def input(self):
        "Input from player"
        while True:
            try:
                # This input only accepts A-I now. Anything else prints the invalid entry message
                self.column = input("Choose a column (A-I): ").upper()
                if self.column in constants.COLUMN_LETTERS:
                    break
                else:
                    print("Invalid entry.")
            except:
                pass

        while True:
            try:
                # This input only accepts 1-9 now. Anything else prints the invalid entry message
                self.row = int(input("Choose a row (1-9): "))
                if self.row in constants.ROW_NUMBERS:
                    print(f"self.row: {self.row}")
                    break
                else:
                    print("Invalid entry.")
            except:
                print("Invalid entry.")

        while True:
            try:
                self.number = int(
                    input("Choose a number to insert in the box (1-9): "))  # This input only accepts 1-9 now. Anything else prints the invalid entry message
                if self.number in constants.ROW_NUMBERS:
                    break
                else:
                    print("Invalid entry.")
            except:
                print("Invalid entry.")
        print(f"self.row: {self.row}")
        # return self
