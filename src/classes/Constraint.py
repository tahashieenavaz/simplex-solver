from src.enums.Sign import Sign


class Constraint:
    def __init__(self, sign: Sign, coefficients: list):
        self.sign = sign
        self.coefficients = coefficients
