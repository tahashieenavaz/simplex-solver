from enums.Objectives import Objectives
from enums.Sign import Sign

from classes.ObjectiveFunction import ObjectiveFunction
from classes.ConstraintBag import ConstraintBag


def main():
    objective = ObjectiveFunction(Objectives.Max, 2, 1)

    constraints = ConstraintBag()
    constraints.add(Sign.SE, 3, -2)
    constraints.add(Sign.SE, 1, 2)

    print(constraints)


if __name__ == "__main__":
    main()
