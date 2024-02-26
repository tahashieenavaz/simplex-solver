from sanitizers.Sanitizer import Sanitizer


class CoefficientCountSanitizer(Sanitizer):
    def __init__(self, data: list, correct_count: int) -> None:
        self.correct_count = correct_count
        self.data = data

    def sanitize(self) -> bool:
        return len(self.data) == self.correct_count
