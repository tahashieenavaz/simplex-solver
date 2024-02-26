class NoAnswerException(Exception):
    def __init__(self) -> None:
        super().__init__("The answer to the problem has not been calculated yet, use \"solve\" method first")
