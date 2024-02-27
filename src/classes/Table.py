import numpy as np
from tabulate import tabulate

from errors.InvalidTableDimensionException import InvalidTableDimensionException
from utils.functions import header_generator


class Table:
    def __init__(self, initial: list | None = None) -> None:
        if bool(initial):
            self.value = np.array(initial)

            if self.value.ndim != 2:
                raise InvalidTableDimensionException
        else:
            self.value = np.array([])

    def shape(self):
        """
        The `shape` function returns the shape of the `value` attribute.
        :return: The `shape` attribute of the `value` object is being returned.
        """
        return self.value.shape

    def rows(self):
        """
        This function returns the number of rows in a matrix.
        :return: The `rows` method is returning the number of rows in the data structure, which is obtained
        by calling the `shape` method and accessing the first element of the returned tuple.
        """
        return self.shape()[0]

    def cols(self):
        """
        The `cols` function returns the number of columns in the shape of the object.
        :return: The `cols` method is returning the number of columns in the shape of the object.
        """
        return self.shape()[1]

    def void(self):
        """
        The function `void` checks if the shape of `self.value` is empty and if its length is 1.
        :return: The code snippet is checking if the shape of the `value` attribute is empty (has 0
        elements) and if the length of the `value` attribute is 1. If both conditions are true, then it
        returns `True`, otherwise it returns `False`.
        """
        return self.value.shape[0] == 0 and len(self.value.shape) == 1

    def transpose(self):
        """
        The `transpose` function returns the transpose of the `value` attribute of the object.
        :return: The code is returning the transpose of the `value` attribute of the object.
        """
        return self.value.T

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

    def add_row(self, new: list):
        """
        The `add_row` function appends a new row to a numpy array.

        :param new: The `add_row` method you provided seems to be adding a new row to a numpy array
        `self.value` using `np.vstack`. The `new` parameter is expected to be a list representing the new
        row that you want to add to the existing array
        :type new: list
        """
        if self.void():
            self.value = np.array(new)
        else:
            self.value = np.vstack([self.value, new])

    def add_col(self, new: list, index=None):
        """
        The `add_col` function appends a new list as a column to an existing numpy array.

        :param new: The `new` parameter in the `add_col` method is expected to be a list that contains the
        values you want to add as a new column to the existing data in the `self.value` attribute
        :type new: list
        """
        if self.void():
            self.value = np.array(new)
        else:
            if index is None:
                index = self.cols()

            self.value = np.insert(self.value, index, new, axis=1)

    def beautify(self, indexlist=[], delimiter="\t"):
        indexlist.insert(0, "-z")

        print(tabulate(
            self.value,
            tablefmt="fancy_grid",
            showindex=indexlist,
            headers=header_generator(self.cols())
        ))
