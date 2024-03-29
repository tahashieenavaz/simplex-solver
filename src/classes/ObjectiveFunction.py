from utils.enums import Objectives

from classes.Collection import Map

from utils.functions import fraction


class ObjectiveFunction:
    def __init__(self, objective: Objectives, *args) -> None:
        self.objective = objective
        self.coeffs = Map(args).using(fraction)

    def isMax(self):
        """
        This function checks if the objective is set to "Max".
        :return: The `isMax` method is returning a boolean value indicating whether the `objective`
        attribute is equal to `Objectives.Max`.
        """
        return self.objective == Objectives.Max

    def isMin(self):
        """
        This function checks if the objective is set to minimize.
        :return: The `isMin` method is returning a boolean value indicating whether the `objective`
        attribute of the object is equal to `Objectives.Min`.
        """
        return self.objective == Objectives.Min

    def variableCount(self):
        """
        This function returns the number of elements in the "coeffs" list of the object.
        :return: The `variableCount` method is returning the length of the `coeffs` attribute of the object.
        """
        return len(self.coeffs)

    def pop(self):
        self.coeffs.pop()
