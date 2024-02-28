from classes.Constraint import Constraint
from classes.Table import Table

from utils.enums import Sign


class ConstraintBag:
    def __init__(self) -> None:
        self.bag = []

    def count(self):
        return len(self.bag)

    def add(self, sign: Sign, rhb: float, *args):
        self.bag.append(Constraint(sign, rhb, args))

    def table(self) -> Table:
        finalTable = []
        for constraint in self.bag:
            finalTable.append(constraint.row())

        return Table(finalTable)
