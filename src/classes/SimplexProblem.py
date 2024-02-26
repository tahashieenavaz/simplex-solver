from classes.ObjectiveFunction import ObjectiveFunction
from classes.ConstraintBag import ConstraintBag
from classes.Table import Table

from collections import Counter

from utils.enums import Sign

from errors.NoAnswerException import NoAnswerException
from errors.NoBaseCalculatedException import NoBaseCalculatedException

from utils.functions import subscript


class SimplexProblem:
    def __init__(self, objective: ObjectiveFunction, constraints: ConstraintBag):
        self.objective = objective
        self.constraints = constraints
        self.isSolved = False
        self.answer = None

        self.base = []
        self.table = Table()

        self.baseTable()
        self.standardize()
        self.formFirstBase()

    def getBaseRepresentation(self):
        return list(map(lambda x: subscript(x), self.base))

    def beautify(self):
        self.table.beautify(indexlist=self.getBaseRepresentation())

    def formFirstBase(self):
        # TODO: check if the number of basis matches the number of constraints, if not go for two phase

        for index, column in enumerate(self.table.value.T):
            countedElements = Counter(column)

            checkIfOnlyZeroAndOneExistInColoumn = list(
                countedElements.keys()) == [0, 1]
            checkIfNumberOfOnesIsOne = countedElements[1] == 1
            checkIfNumberOfZerosMatch = countedElements[0] == self.table.rows(
            ) - 1

            if checkIfOnlyZeroAndOneExistInColoumn and checkIfNumberOfOnesIsOne and checkIfNumberOfZerosMatch:
                self.base.append(index)

    def baseTable(self):
        first_column = [0]

        if self.objective.isMax():
            objective_function_coefficients = list(
                map(lambda x: -x, self.objective.coeffs))
        else:
            objective_function_coefficients = self.objective.coeffs

        self.table.add_row(objective_function_coefficients)

        for constraint in self.constraints.bag:
            self.table.add_row(constraint.coeffs)
            first_column.append(constraint.rhb)

        self.table.add_col(first_column, 0)

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
        # TODO: complete

        self.isSolved = True
