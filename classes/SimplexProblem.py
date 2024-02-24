from ObjectiveFunction import ObjectiveFunction
from SimplexAnswer import SimplexAnswer
from ConstraintCollection import ConstraintCollection


class SimplexProblem:
    def __init__(self, objective_function: ObjectiveFunction, constraints: ConstraintCollection) -> SimplexAnswer:
        self.objective_function = objective_function
        self.objective_function = objective_function
        self.constraints = constraints
