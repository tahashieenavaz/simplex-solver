from utils.functions import sanitize
from sanitizers.CoefficientCountSanitizer import CoefficientCountSanitizer


def main():
    print(sanitize(CoefficientCountSanitizer,
          correct_count=4, data=[2, 3, 4, 5, 22  ]))


if __name__ == "__main__":
    main()
