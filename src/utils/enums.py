from enum import Enum


class Objectives(Enum):
    Max = "max"
    Min = "min"


class Sign(Enum):
    GREATEREQUAL = ">="
    GreaterEqual = ">="
    GE = ">="

    GREATER = ">"
    Greater = ">"
    G = ">"

    SMALLEREQUAL = "<="
    SmallerEqual = "<="
    SE = "<="

    SMALLER = "<"
    Smaller = "<"
    S = "<"

    EQUAL = "="
    Equal = "="
    E = "="
