from classes.SimplexProblem import SimplexProblem
from classes.ConstraintBag import ConstraintBag
from classes.ObjectiveFunction import ObjectiveFunction


class DualSimplexProblem(SimplexProblem):
    def __init__(self, objective: ObjectiveFunction, constraints: ConstraintBag):
        super().__init__(objective, constraints)

    def isOptimal(self) -> bool:
        return all(item >= 0 for item in self.table.col(0))