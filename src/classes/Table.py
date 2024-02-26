import numpy as np
from errors.InvalidTableDimensionException import InvalidTableDimensionException


class Table:
    def __init__(self, initial) -> None:
        self.value = np.array(initial)
        self.shape = self.value.shape

        if self.value.ndim != 2:
            raise InvalidTableDimensionException
