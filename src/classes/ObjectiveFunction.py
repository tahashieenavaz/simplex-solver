from enums.Objectives import Objectives


class ObjectiveFunction:
    def __init__(self, objective: Objectives, *args) -> None:
        self.objective = objective
        self.coeffs = args

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
