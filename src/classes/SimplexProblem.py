from classes.ObjectiveFunction import ObjectiveFunction
from classes.ConstraintBag import ConstraintBag
from classes.Table import Table
from enums.Sign import Sign
from errors.NoAnswerException import NoAnswerException


class SimplexProblem:
    def __init__(self, objective: ObjectiveFunction, constraints: ConstraintBag):
        self.objective = objective
        self.constraints = constraints
        self.isSolved = False
        self.answer = None

        self.table = Table()

        self.base_table()
        self.standardize()

    def base_table(self):
        self.table.add_row(self.objective.coeffs)

        for constraint in self.constraints.bag:
            self.table.add_row(constraint.coeffs)

    def standardize(self):
        for index, constraint in enumerate(self.constraints.bag):
            new_column = [0] * self.table.rows()
            print(new_column)

            if constraint.sign == Sign.GreaterEqual:
                new_column[index + 1] = -1
            elif constraint.sign == Sign.SmallerEqual:
                new_column[index + 1] = 1

            self.table.add_col(new_column)

    def solve(self) -> None:
        # TODO: complete

        self.isSolved = True
