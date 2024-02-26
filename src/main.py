from enums.Objectives import Objectives
from enums.Sign import Sign

from classes.ObjectiveFunction import ObjectiveFunction
from classes.ConstraintBag import ConstraintBag
from classes.SimplexProblem import SimplexProblem


def main():
    objective = ObjectiveFunction(Objectives.Max, 2, 1)

    constraints = ConstraintBag()
    constraints.add(Sign.SmallerEqual, 0, 3, -2)
    constraints.add(Sign.SmallerEqual, 6, 1, 2)

    problem = SimplexProblem(objective, constraints)
    problem.solve()

    problem.beautify()


if __name__ == "__main__":
    main()
