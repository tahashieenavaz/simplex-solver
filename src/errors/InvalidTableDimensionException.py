# The `InvalidTableDimensionException` class is a custom exception in Python that is raised when a
# table is not a two-dimensional array.

class InvalidTableDimensionException(Exception):
    def __init__(self) -> None:
        super().__init__("Tables need to be two dimensional arrays")
