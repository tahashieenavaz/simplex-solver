import numpy as np
from errors.InvalidTableDimensionException import InvalidTableDimensionException
from utils.functions import newline
from utils.functions import log


class Table:
    def __init__(self, initial: list) -> None:
        self.value = np.array(initial)
        self.shape = self.value.shape

        if self.value.ndim != 2:
            raise InvalidTableDimensionException

    def row(self, index: int):
        """
        The `row` function returns a specific row from a matrix-like object based on the given index.

        :param index: The `index` parameter in the `row` method is an integer that represents the index of
        the row you want to retrieve from the `value` attribute
        :type index: int
        :return: The `row` method is returning a specific row from a 2D array or matrix represented by
        `self.value`. The row being returned is specified by the `index` parameter, and it is returned as a
        1D array or list.
        """
        return self.value[index, :]

    def col(self, index: int):
        """
        The function `col` returns the values in a specific column of a 2D array.

        :param index: The `index` parameter in the `col` method represents the column index of the 2D array
        or matrix from which you want to extract the values
        :type index: int
        :return: The `col` method is returning the values in a specific column of a matrix-like object. It
        takes an index as input and returns all the values in that column.
        """
        return self.value[:, index]

    def change_col(self, index: int, new) -> None:
        """
        This function changes the values in a specific column of a 2D array with the provided new values.

        :param index: The `index` parameter in the `change_col` method represents the column index in a 2D
        array where you want to change the values
        :type index: int
        :param new: The `new` parameter in the `change_col` method represents the new values that you want
        to assign to the specified column at the given index in the `self.value` array
        """
        self.value[:, index] = new

    def change_row(self, index: int, new) -> None:
        """
        This function changes a specific row in a 2D array with the provided new values.

        :param index: The `index` parameter in the `change_row` method is an integer that represents the
        index of the row that you want to change in the matrix or 2D array
        :type index: int
        :param new: The `new` parameter in the `change_row` method represents the new values that you want
        to assign to a specific row in a 2D array or matrix. When you call the `change_row` method with an
        index and a new row of values, it will update the specified row at
        """
        self.value[index, :] = new

    def beautify(self, delimiter="\t"):
        """
        The `beautify` function in Python prints the values of a matrix with a specified delimiter between
        elements.
        
        :param delimiter: The `delimiter` parameter in the `beautify` method is used to specify the
        character or string that will be used to separate the values when they are printed. By default, the
        delimiter is set to a tab character ("\t"), but you can provide a different delimiter if needed,
        defaults to \t (optional)
        """
        rows, cols = self.shape

        for i in range(rows):
            for p in range(cols):
                log(f"{self.value[i][p]}{delimiter}")

            newline()
