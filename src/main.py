from utils.functions import sanitize
from sanitizers.CoefficientCountSanitizer import CoefficientCountSanitizer


def main():
    sanitize([2, 3, 4], CoefficientCountSanitizer, 4)


if __name__ == "__main__":
    main()
