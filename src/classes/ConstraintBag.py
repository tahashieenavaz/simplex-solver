from classes.Constraint import Constraint
from enums.Sign import Sign


class ConstraintBag:
    def __init__(self) -> None:
        self.bag = []

    def add(self, sign: Sign, *args):
        self.bag.append(Constraint(sign, args))