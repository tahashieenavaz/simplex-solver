from classes.SimplexProblem import SimplexProblem
from classes.ConstraintBag import ConstraintBag
from classes.ObjectiveFunction import ObjectiveFunction


class TwoPhaseSimplexProblem(SimplexProblem):
    def __init__(self, objective: ObjectiveFunction, constraints: ConstraintBag):
        newObjectiveFunctionCoefficients = [0] * objective.variableCount() + \
            [1] * constraints.count()
        newObjectiveFunction = ObjectiveFunction(
            objective, newObjectiveFunctionCoefficients)

        newConstraints = constraints.table()
        for i in range(constraints.count()):
            diffrence = constraints.count() - i
            newConstraints.add_col([0] * i + [1] + [0] * diffrence)

        self.engine(newObjectiveFunction, newConstraints)
        self.baseTable()
        self.formFirstBase()
