from classes.ObjectiveFunction import ObjectiveFunction
from classes.SimplexAnswer import SimplexAnswer
from classes.ConstraintCollection import ConstraintCollection


class SimplexProblem:
    def __init__(self, objective_function: ObjectiveFunction, constraints: ConstraintCollection) -> SimplexAnswer:
        self.objective_function = objective_function
        self.objective_function = objective_function
        self.constraints = constraints
