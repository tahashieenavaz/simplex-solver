from classes.Constraint import Constraint
from utils.enums import Sign


class ConstraintBag:
    def __init__(self) -> None:
        self.bag = []

    def add(self, sign: Sign, rhb: float, *args):
        self.bag.append(Constraint(sign, rhb, args))
