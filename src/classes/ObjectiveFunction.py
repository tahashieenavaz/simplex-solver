from enums.Objectives import Objectives


class ObjectiveFunction:
    def __init__(self, target: Objectives, *args) -> None:
        self.target = target
        self.coefficients = args
