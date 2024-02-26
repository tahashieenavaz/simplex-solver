from classes.ObjectiveFunction import ObjectiveFunction
from classes.SimplexAnswer import SimplexAnswer
from src.classes.ConstraintBag import ConstraintCollection
from errors.NoAnswerException import NoAnswerException


class SimplexProblem:
    def __init__(self, objective_function: ObjectiveFunction, constraints: ConstraintCollection):
        self.objective_function = objective_function
        self.constraints = constraints
        self.isSolved = False
        self.answer = None

    def solve(self) -> None:
        pass

    def answer(self):
        if self.isSolved:
            return self.answer

        raise NoAnswerException
