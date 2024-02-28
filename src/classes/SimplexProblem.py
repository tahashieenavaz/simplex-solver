from classes.ObjectiveFunction import ObjectiveFunction
from classes.ConstraintBag import ConstraintBag
from classes.PivotElement import PivotElement
from classes.Basis import Basis
from classes.Table import Table

from collections import Counter

from utils.enums import Sign

from errors.NoAnswerException import NoAnswerException
from errors.NoBaseCalculatedException import NoBaseCalculatedException

from utils.functions import subscript
from utils.functions import panicIfNot


class SimplexProblem:
    def __init__(self, objective: ObjectiveFunction, constraints: ConstraintBag):
        self.objective = objective
        self.constraints = constraints
        self.isSolved = False
        self.answer = None

        self.basis = Basis()
        self.table = Table()

        self.baseTable()
        self.standardize()
        self.formFirstBase()

    def beautify(self) -> None:
        self.table.beautify(indexlist=self.basis.representation())

    def formFirstBase(self) -> None:
        # TODO: check if the number of basis matches the number of constraints, if not go for two phase

        for index, column in enumerate(self.table.value.T):
            countedElements = Counter(column)

            checkIfOnlyZeroAndOneExistInColoumn = list(
                countedElements.keys()) == [0, 1]
            checkIfNumberOfOnesIsOne = countedElements[1] == 1
            checkIfNumberOfZerosMatch = countedElements[0] == self.table.rows(
            ) - 1

            if checkIfOnlyZeroAndOneExistInColoumn and checkIfNumberOfOnesIsOne and checkIfNumberOfZerosMatch:
                self.basis.add(index)

    def baseTable(self) -> None:
        """
        The function `baseTable` constructs a table with objective function coefficients and constraint
        coefficients along with their corresponding right-hand side values.
        """
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

    def isOptimal(self) -> bool:
        """
        The function `isOptimal` checks if all items in the first row of a table are greater than 0.
        :return: The `isOptimal` method is returning a boolean value. It checks if all items in the first
        row of the table are greater than 0, and returns `True` if this condition is met for all items,
        otherwise it returns `False`.
        """
        return all(item > 0 for item in self.table.row(0))

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
            new_column = [0] * self.table.rows()

            if constraint.sign == Sign.GreaterEqual:
                new_column[index + 1] = -1
            elif constraint.sign == Sign.SmallerEqual:
                new_column[index + 1] = 1

            self.table.add_col(new_column)

    def solve(self) -> None:
        pivot = PivotElement()

        while self.isNotOptimal():
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
            
            self.beautify()

            self.basis.swap(
                self.basis.variables[pivot.row],
                pivot.col
            )

            self.beautify()
            break


            # DO Linear Operations

        self.isSolved = True
