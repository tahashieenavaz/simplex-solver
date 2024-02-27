class PivotElement:
    def __init__(self) -> None:
        self.row = -1
        self.col = -1
        self.lastTheta = None
        self.value = None

    def setCol(self, index: int):
        """
        The function `setCol` sets the value of the `col` attribute to the specified index.

        :param index: The `index` parameter in the `setCol` method is an integer that represents the index
        of the column that you want to set
        :type index: int
        """
        self.col = index

    def setRow(self, index: int, theta: float, value: float):
        """
        The `setRow` function in Python sets the value of the `row` attribute to the specified index.

        :param index: The `setRow` method you provided takes an integer `index` as a parameter. This `index`
        parameter is used to set the `row` attribute of the object to the value of the `index` parameter
        :type index: int
        """
        if self.lastTheta is None:
            self.row = index
            self.lastTheta = theta
            self.value = value
            return

        if theta < self.lastTheta:
            self.row = index
            self.lastTheta = theta
            self.value = value
            return

    def isRowValid(self):
        """
        The function `isRowValid` checks if the row attribute is not equal to -1.
        :return: The `isRowValid` method is returning a boolean value that indicates whether the `row`
        attribute of the object is not equal to -1.
        """
        return not self.row == -1

    def isColValid(self):
        """
        The function `isColValid` returns True if the column is not equal to -1.
        :return: The function `isColValid` is returning a boolean value indicating whether the attribute
        `col` is not equal to -1.
        """
        return not self.col == -1

    def isValid(self):
        """
        The `isValid` function checks if -1 is not present in the `row` and `col` attributes of the object.
        :return: The `isValid` method is returning a boolean value indicating whether -1 is not present in
        the list `[self.row, self.col]`.
        """
        return self.isRowValid() and self.isColValid()

    def __str__(self) -> str:
        return f"{self.row} {self.col}"
