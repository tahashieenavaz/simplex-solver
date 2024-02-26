class InvalidCoefficientCountException(Exception):
    def __init__(self) -> None:
        super().__init__("The number of coefficients provided does not match the expected count")
