from classes.ObjectiveFunction import ObjectiveFunction
from classes.ConstraintBag import ConstraintBag
from classes.PivotElement import PivotElement
from classes.Basis import Basis
from classes.Table import Table
from classes.SimplexAnswer import SimplexAnswer
from classes.Collection import Map

from collections import Counter

from utils.enums import Sign

from utils.functions import panicIfNot
from utils.functions import fraction


class SimplexProblem:
    def __init__(self, objective: ObjectiveFunction, constraints: ConstraintBag):
        self.engine(objective, constraints)
        self.baseTable()
        self.standardize()
        self.formFirstBase()

    def engine(self, objective: ObjectiveFunction, constraints: ConstraintBag):
        self.objective = objective
        self.constraints = constraints
        self.isSolved = False
        self.answer = SimplexAnswer()
        self.basis = Basis()
        self.table = Table()

    def beautify(self) -> None:
        self.table.beautify(indexlist=self.basis.representation())

    def formFirstBase(self) -> None:
        for index, column in enumerate(self.table.transpose()):
            countedElements = Counter(column)

            checkIfOnlyZeroAndOneExistInTheColumn = list(
                countedElements.keys()).sort() == [0, 1].sort()
            checkIfNumberOfOnesIsOne = countedElements[1] == 1
            checkIfNumberOfZerosMatch = countedElements[0] == self.table.rows(
            ) - 1
            if checkIfOnlyZeroAndOneExistInTheColumn and checkIfNumberOfOnesIsOne and checkIfNumberOfZerosMatch:
                self.basis.add(index)

    def baseTable(self) -> None:
        """
        The function `baseTable` constructs a table with objective function coefficients and constraint
        coefficients along with their corresponding right-hand side values.
        """
        first_column = [fraction(0)]

        if self.objective.isMax():
            objective_function_coefficients = Map(
                self.objective.coeffs).using(lambda x: fraction(-x))
        else:
            objective_function_coefficients = self.objective.coeffs

        self.table.add_row(objective_function_coefficients)

        for constraint in self.constraints.bag:
            self.table.add_row(constraint.coeffs)
            first_column.append(constraint.rhb)

        self.table.add_col(first_column, 0)

    def isOptimal(self) -> bool:
        """
        The function `isOptimal` checks if all items in the first row of a table are greater than 0.
        :return: The `isOptimal` method is returning a boolean value. It checks if all items in the first
        row of the table are greater than 0, and returns `True` if this condition is met for all items,
        otherwise it returns `False`.
        """
        return all(item >= 0 for item in self.table.row(0))

    def isNotOptimal(self) -> bool:
        """
        The function `isNotOptimal` returns the opposite boolean value of the function `isOptimal`.
        :return: The `isNotOptimal` method is returning the opposite of the result of the `isOptimal`
        method. If `self.isOptimal()` returns `True`, then `isNotOptimal` will return `False`. If
        `self.isOptimal()` returns `False`, then `isNotOptimal` will return `True`.
        """
        return not self.isOptimal()

    def standardize(self) -> None:
        """
        The `standardize` function adds a new column to a table based on the sign of a constraint.
        """
        for index, constraint in enumerate(self.constraints.bag):
            if constraint.sign == Sign.Equal:
                continue

            new_column = [fraction(0)] * self.table.rows()

            if constraint.sign == Sign.GreaterEqual:
                new_column[index + 1] = fraction(-1)
            elif constraint.sign == Sign.SmallerEqual:
                new_column[index + 1] = fraction(1)

            self.table.add_col(new_column)

    def solve(self) -> None:
        self.beautify()

        while self.isNotOptimal():
            pivot = PivotElement()
            for i in range(1, self.table.cols()):
                if self.table.row(0)[i] < 0:
                    pivot.setCol(i)
                    break
            panicIfNot(pivot.isColValid())

            for index, element in enumerate(self.table.transpose()[pivot.col]):
                if element <= 0:
                    continue

                theta = self.table.col(0)[index] / element
                pivot.setRow(index, theta, element)
            panicIfNot(pivot.isValid())

            self.table.change_row(
                pivot.row,
                self.table.row(pivot.row) * (1 / pivot.value)
            )

            self.basis.swap(
                self.basis.variables[pivot.row - 1],
                pivot.col
            )

            baseRowForLinearOperations = self.table.row(pivot.row)
            for i in range(self.table.rows()):
                if i == pivot.row:
                    continue

                rowForTheLinearOperation = baseRowForLinearOperations * \
                    -1 * self.table.col(pivot.col)[i]
                self.table.change_row(
                    i, rowForTheLinearOperation + self.table.row(i))

            self.beautify()

        self.answer.record(self.table)
        self.isSolved = True
