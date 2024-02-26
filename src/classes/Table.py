import numpy as np
from errors.InvalidTableInputException import InvalidTableInputException


class Table:
    def __init__(self, initial) -> None:
        self.value = np.array(initial)

        if self.value.shape[0] < 2:
            raise InvalidTableInputException
