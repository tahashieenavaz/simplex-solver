from classes.PivotElement import PivotElement


class DualSimplexPivotElement(PivotElement):
    def __init__(self) -> None:
        super().__init__()

    def setRow(self, index: int) -> None:
        self.row = index

    def setCol(self, index: int, theta: float, value: float) -> None:
        if theta < self.lastTheta:
            self.lastTheta = theta
            self.col = index
            self.value = value
            return
