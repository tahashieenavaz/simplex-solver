from classes.SimplexProblem import SimplexProblem
from classes.ConstraintBag import ConstraintBag
from classes.ObjectiveFunction import ObjectiveFunction

from collections import Counter

from utils.functions import fraction

import numpy as np

from utils.enums import Objectives


class TwoPhaseSimplexProblem(SimplexProblem):
    def __init__(self, objective: ObjectiveFunction, constraints: ConstraintBag):
        self.originalVariableCount = objective.variableCount()
        self.originalConstraintCount = constraints.count()
        self.originalObjectiveFunction = objective

        newObjectiveFunctionCoefficients = [0] * objective.variableCount() + \
            [1] * constraints.count()
        newObjectiveFunction = ObjectiveFunction(
            objective.objective, *newObjectiveFunctionCoefficients)

        for index, constraint in enumerate(constraints.bag):
            difference = constraints.count() - index - 1
            constraint.append([fraction(0)] * index +
                              [fraction(1)] + [fraction(0)] * difference)

        self.engine(newObjectiveFunction, constraints)
        self.baseTable()
        self.formFirstBase()
        self.transformFirstRow()

    def formFirstBase(self) -> None:
        for i in range(self.originalVariableCount + 1, self.originalVariableCount + 1 + self.originalConstraintCount):
            self.basis.add(i)

    def transformFirstRow(self):
        transformationRow = np.array([fraction(0)] * self.table.cols())
        for i in range(1, self.table.rows()):
            transformationRow += self.table.row(i)
        transformationRow *= -1
        firstRow = self.table.row(0)
        firstRow = firstRow + transformationRow
        self.table.change_row(0, firstRow)

    def solve(self):
        super().solve()

        for i in range(self.originalConstraintCount):
            self.table.popColumn()

        objectiveFunctionSign = 1
        if self.originalObjectiveFunction.objective == Objectives.Max:
            objectiveFunctionSign = -1

        for i in range(1, self.table.cols()):
            self.table.value[0][i] = objectiveFunctionSign * \
                self.originalObjectiveFunction.coeffs[i - 1]

        self.beautify()

        super().solve()
