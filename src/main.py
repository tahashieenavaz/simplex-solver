from classes.Table import Table
from utils.functions import sanitize
from enums.Objectives import Objectives
from classes.ObjectiveFunction import ObjectiveFunction
from classes.ConstraintBag import ConstraintBag


def main():
    objective = ObjectiveFunction(Objectives.Max, 2, 1)

    constraints = ConstraintBag()
    constraints.add(3, 4)

    print(constraints)


if __name__ == "__main__":
    main()
