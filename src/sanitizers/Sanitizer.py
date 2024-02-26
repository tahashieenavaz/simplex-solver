class Sanitizer:
    def __init__(self) -> None:
        self.exception = Exception

    def condition(self) -> bool:
        return False

    def sanitize(self) -> None:
        if not self.condition():
            raise self.exception
