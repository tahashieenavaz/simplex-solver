from utils.enums import Objectives
from utils.enums import Sign

from classes.ObjectiveFunction import ObjectiveFunction
from classes.ConstraintBag import ConstraintBag
from classes.SimplexProblem import SimplexProblem
from classes.TwoPhaseSimplexProblem import TwoPhaseSimplexProblem


def main():
    # # Normal Simplex
    # objective = ObjectiveFunction(Objectives.Max, 2, 1)
    # constraints = ConstraintBag()
    # constraints.add(Sign.SmallerEqual, 0, 3, -2)
    # constraints.add(Sign.SmallerEqual, 6, 1, 2)

    # problem = SimplexProblem(objective, constraints)
    # problem.solve()

    # Two Phase Simplex
    objective = ObjectiveFunction(Objectives.Min, 1, -2, 0)
    constraints = ConstraintBag()
    constraints.add(Sign.Equal, 1, 2, 1, -3)
    constraints.add(Sign.Equal, 5, 3, 2, -1)

    problem = TwoPhaseSimplexProblem(objective, constraints)
    problem.solve()


if __name__ == "__main__":
    main()
