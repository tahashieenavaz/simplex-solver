from enums.Objectives import Objectives


class ObjectiveFunction:
    def __init__(self, objective: Objectives, *args) -> None:
        self.objective = objective
        self.coeffs = args
