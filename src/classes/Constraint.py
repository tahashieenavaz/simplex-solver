from enums.Sign import Sign


class Constraint:
    def __init__(self, sign: Sign, coeffs: list):
        self.sign = sign
        self.coeffs = coeffs
