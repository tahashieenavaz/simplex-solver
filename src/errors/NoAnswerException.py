# This class defines a custom exception called `NoAnswerException` that is raised when the answer to a
# problem has not been calculated yet.

class NoAnswerException(Exception):
    def __init__(self) -> None:
        super().__init__("The answer to the problem has not been calculated yet, use \"solve\" method first")
