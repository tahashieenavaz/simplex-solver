class NoBaseCalculatedException(Exception):
    def __init__(self) -> None:
        super().__init__("No base has been calculated use, \"formFirstBase\" first")
