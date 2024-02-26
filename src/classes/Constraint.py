from utils.enums import Sign


class Constraint:
    def __init__(self, sign: Sign, rhb: float, coeffs: list):
        self.sign = sign
        self.coeffs = coeffs
        self.rhb = rhb
