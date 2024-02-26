class InvalidTableDimensionException(Exception):
    def __init__(self) -> None:
        super().__init__("Tables need to be two dimensional arrays")
