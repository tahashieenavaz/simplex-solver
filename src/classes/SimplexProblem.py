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

        self.baseTable()
        self.standardize()

    def baseTable(self):
        if self.objective.isMax():
            objective_function_coefficients = list(
                map(lambda x: -x, self.objective.coeffs))
        else:
            objective_function_coefficients = self.objective.coeffs

        self.table.add_row(objective_function_coefficients)

        for constraint in self.constraints.bag:
            self.table.add_row(constraint.coeffs)

    def isOptimal(self):
        return all(item > 0 for item in self.table.row(0))

    def isNotOptimal(self):
        return not self.isOptimal()

    def standardize(self):
        for index, constraint in enumerate(self.constraints.bag):
            new_column = [0] * self.table.rows()

            if constraint.sign == Sign.GreaterEqual:
                new_column[index + 1] = -1
            elif constraint.sign == Sign.SmallerEqual:
                new_column[index + 1] = 1

            self.table.add_col(new_column)

    def solve(self) -> None:
        while (self.isNotOptimal()):
            self.findPivot()

        self.isSolved = True
