class FractionalNumber:
    def __init__(self, numerator: float, denominator: float) -> None:
        self.numerator = numerator
        self.denominator = denominator
        self.value = self.numerator / self.denominator

    def __repr__(self) -> str:
        return f"{self.numerator}⁄{self.denominator}"
