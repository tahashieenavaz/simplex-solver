from classes.Table import Table
from utils.functions import sanitize


def main():
    a = sanitize("CoefficientCount", data=[1, 2, 3, 4], correct_count=3)
    print(a)
    table = Table([[1, 2], [3, 4]])
    table.beautify()


if __name__ == "__main__":
    main()
