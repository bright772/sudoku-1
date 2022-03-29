from text import Prompts


class SelectAction:
    """Prompts a number with an action.
    The user needs to select an action to play."""

    def __init__(self):
        self.instruction = 0

    def actions(self):
        "Displays action. User enters a number."
        print("\n1. Play game")
        print("2. Delete a number")
        print("3. Exit game\n")
        self.instruction = int(input("Enter a number, selecting an action: "))


class Action(SelectAction):
    "Acts according to selected action"

    def __init__(self):
        super().__init__()
        self.prompt = Prompts()

    def todo(self):
        "Determines what to do according to user's input"

        if self.instruction == 1:
            print(self.prompt.input())

        elif self.instruction == 2:
            print(self.prompt.input())

        elif self.instruction == 3:
            print("Game Over. Thanks for playing.")
