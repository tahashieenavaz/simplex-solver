from utils.enums import Sign

from classes.Collection import Map

from utils.functions import fraction


class Constraint:
    def __init__(self, sign: Sign, rhb: float, coeffs: list):
        self.sign = sign
        self.rhb = fraction(rhb)
        self.coeffs = Map(coeffs).using(fraction)

    def row(self):
        return [self.rhb, *self.coeffs]

    def pop(self):
        self.coeffs.pop()

    def append(self, newSet: list):
        self.coeffs = self.coeffs + newSet

    def __repr__(self) -> str:
        return f"{self.rhb} {self.coeffs}"
