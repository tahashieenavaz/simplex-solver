from utils.functions import subscript
from classes.Collection import Map


class Basis:
    def __init__(self) -> None:
        self.variables = []

    def add(self, variable: int) -> None:
        """
        The `add` function appends an integer variable to a list within the object.

        :param variable: The `add` method takes an integer `variable` as a parameter and appends it to the
        `variables` list within the class instance
        :type variable: int
        """
        self.variables.append(variable)

    def representation(self) -> list:
        """
        The `representation` function returns a list of subscripted elements from the `base` attribute using
        a lambda function.
        :return: A list of elements obtained by applying the `subscript` function to each element in the
        `self.base` list.
        """
        return Map(self.variables).using(subscript)

    def swap(self, leaving: int, entering: int) -> None:
        """
        The `swap` function takes two integers, `leaving` and `entering`, and replaces the first occurrence
        of `leaving` in the list `self.variables` with `entering`.

        :param leaving: The `leaving` parameter in the `swap` method represents the variable that you want
        to replace in the list of variables with another variable
        :type leaving: int
        :param entering: The `entering` parameter in the `swap` method represents the value that will
        replace the value specified by the `leaving` parameter in the list `self.variables`
        :type entering: int
        """
        self.variables[self.variables.index(leaving)] = entering
