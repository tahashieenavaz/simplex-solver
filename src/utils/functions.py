import importlib
from sanitizers.Sanitizer import Sanitizer
from fractions import Fraction

from utils.settings import Settings


def env(key) -> None | str:
    if key in Settings:
        return Settings[key]

    return None


def showFractionalIfNeeded(number: str):
    """
    The function `showFractionalIfNeeded` removes the denominator if it is equal to 1 from a given
    fractional number.

    :param number: The `showFractionalIfNeeded` function takes a string `number` as input and checks if
    it ends with "/1". If it does, it returns the number without the "/1" suffix; otherwise, it returns
    the original number
    :type number: str
    :return: The function `showFractionalIfNeeded` is returning the input `number` without the "/1"
    suffix if the input ends with "/1". If the input does not end with "/1", the function returns the
    input `number` as is.
    """
    if number.endswith("/1"):
        return number.split("/1")[0]

    return number


def fraction(text: str | int):
    """
    The function `fraction` takes a string or integer input, converts it to a fraction format, and
    returns a `Fraction` object.

    :param text: The `fraction` function takes a parameter `text`, which can be either a string or an
    integer. If `text` is an integer, it is converted to a string. If `text` does not contain a "/", it
    appends "/1" to it. Then it splits the text at
    :type text: str | int
    :return: The code snippet provided defines a function `fraction` that takes a parameter `text` which
    can be either a string or an integer. The function first checks if the input `text` is not a string,
    it converts it to a string. Then, it checks if the string contains a "/", if not, it appends "/1" to
    the string.
    """
    if not isinstance(text, str):
        text = str(text)

    if "/" not in text:
        text += "/1"

    numerator, denominator = text.split("/")
    return Fraction(int(numerator), int(denominator))


def sanitize(sanitizer_class: str, **kwargs) -> bool:
    """
    The `sanitize` function creates an instance of a specified `Sanitizer` class with given keyword
    arguments and calls its `sanitize` method.

    :param sanitizer_class: The `sanitizer_class` parameter in the `sanitize` function is expected to be
    a class that implements a sanitizer. This class should have a constructor that accepts keyword
    arguments (`**kwargs`) and a `sanitize` method that performs the sanitization process
    :type sanitizer_class: Sanitizer
    :return: The function `sanitize` is returning a boolean value, which is the result of calling the
    `sanitize` method on an instance of the `sanitizer_class` class.
    """
    sanitizer_full_classname = f"{sanitizer_class}Sanitizer"
    module = importlib.import_module(f'sanitizers.{sanitizer_full_classname}')
    sanitizer_class_definition = getattr(module, sanitizer_full_classname)
    instance = sanitizer_class_definition(**kwargs)
    return instance.sanitize()


def newline():
    """
    The `newline()` function in Python is used to print a blank line.
    """
    print()


def log(message: str):
    """
    The `log` function in Python is used to print a message without adding a new line character at the
    end.

    :param message: A string parameter named "message"
    :type message: str
    """
    print(message, end="")


def header_generator(count):
    return ["", "x₁", "x₂", "x₃", "x₄", "x₅", "x₆", "x₇", "x₈", "x₉", "x₁₀"][0:count]


def subscript(number=0):
    """
    The function `subscript` converts a given number into subscript format using Unicode characters.

    :param number: The `subscript` function takes a number as input and converts each digit of the
    number into a subscript equivalent. For example, if you pass the number 123, it will return "x₁₂₃",
    defaults to 0 (optional)
    :return: The `subscript` function takes a number as input (default is 0) and converts each digit in
    the number to its subscript equivalent. For example, if the input number is 123, the function will
    return "x₁₂₃".
    """
    final = "x"
    subscriptMap = {
        "0": "₀",
        "1": "₁",
        "2": "₂",
        "3": "₃",
        "4": "₄",
        "5": "₅",
        "6": "₆",
        "7": "₇",
        "8": "₈",
        "9": "₉",
    }
    for digit in str(number):
        final += subscriptMap[digit]

    return final


def panicIf(condition, exception=Exception):
    """
    The function `panicIf` raises an exception if a specified condition is met.

    :param condition: The `condition` parameter is a boolean expression that is evaluated. If the
    condition is `True`, the function will raise an exception based on the `exception` parameter
    :param exception: The `exception` parameter in the `panicIf` function is the type of exception that
    will be raised if the `condition` evaluates to `True`. By default, it is set to `Exception`, but you
    can provide a different exception type when calling the function if needed
    """
    if condition:
        raise exception


def panicIfNot(condition, exception=Exception):
    """
    The function `panicIfNot` raises an exception if a specified condition is not met.

    :param condition: The `condition` parameter is a boolean expression that is evaluated. If the
    condition evaluates to `False`, the function will raise an exception
    :param exception: The `exception` parameter in the `panicIfNot` function is a placeholder for the
    type of exception that will be raised if the `condition` is not met. By default, it is set to
    `Exception`, which is a built-in base class for all exceptions in Python. You can customize
    """
    if not condition:
        raise exception
