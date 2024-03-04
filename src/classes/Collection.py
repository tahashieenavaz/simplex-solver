from typing import Self


class Map:
    def __init__(self, target: list | map) -> None:
        self.target = target

    def using(self, callback) -> list:
        """
        The `using` function takes a callback function as input and applies it to each element in the
        `target` list, returning a new list with the results.

        :param callback: The `callback` parameter in the `using` method is a function that will be applied
        to each element in the `target` attribute of the object
        :return: A list is being returned, where each element is the result of applying the callback
        function to each element in the "target" attribute of the object.
        """
        return list(map(callback, self.target))

    def pipe(self, callback) -> Self:
        """
        The `pipe` function takes a callback function as input and applies it to each element in the target
        list using the `map` function.

        :param callback: The `callback` parameter in the `pipe` method is a function that will be applied to
        each element in the `self.target` list using the `map` function. The result will be a new list with
        the transformed elements
        :return: The `pipe` method is returning a `Map` object that applies the `callback` function to each
        element in the `self.target` iterable.
        """
        return Map(map(callback, self.target))

    def get(self) -> list:
        """
        The `get` function returns the elements of `self.target` as a list.
        :return: A list containing the elements of the "target" attribute is being returned.
        """
        return list(self.target)
