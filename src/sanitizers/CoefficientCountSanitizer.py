class CoefficientCountSanitizer:
    def __init__(self, data, correct_count: int) -> None:
        self.correct_count = correct_count
        self.data = data

    def sanitize(self):
        return len(self.data) == self.correct_count
