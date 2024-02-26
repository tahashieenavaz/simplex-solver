from sanitizers.Sanitizer import Sanitizer
from errors.InvalidCoefficientCountException import InvalidCoefficientCountException


class CoefficientCountSanitizer(Sanitizer):
    def __init__(self, data: list, correct_count: int) -> None:
        self.correct_count = correct_count
        self.data = data
        self.exception = InvalidCoefficientCountException

    def condition(self):
        return len(self.data) == self.correct_count

