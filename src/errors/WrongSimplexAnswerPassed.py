class WrongSimplexAnswerPassed(Exception):
    def __init__(self) -> None:
        super().__init__("A not optimal answer was passed to the class SimplexAnswer")