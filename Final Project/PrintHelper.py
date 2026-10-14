# This class prints lines at set indentations and keeps track of the current indentation level

class PrintHelper():
    #Initializes the PrintHelper, sets indentatin to 0
    def __init__(self) -> None:
        self.currentLevel = 0

    # Increments indentation by one and displays header for the block
    def LevelStart(self, message: str = "----------") -> None:
        self.LevelPrint(message)
        self.currentLevel += 1

    # Prints a message at the current indentation
    def LevelPrint(self, message: str = "") -> None:
        print(self.GenerateIndent() + message)

    # Just like the input() function, but with indentation included
    def LevelInput(self, message: str = "") -> str:
        print(self.GenerateIndent() + message, end="")
        return input()

    # Decreases indentation by one and displays footer for the block
    def LevelEnd(self, message: str = "") -> None:
        if self.currentLevel == 0: raise BaseException("Indent level decreased past zero!")
        self.currentLevel -= 1
        self.LevelPrint(message)

    # Generates the indent prefix for the current indent level
    def GenerateIndent(self) -> str:
        indent = ""
        levelCount = 0
        while levelCount < self.currentLevel:
            indent += "| "
            levelCount += 1
        return indent