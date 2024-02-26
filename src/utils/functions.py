import importlib
from sanitizers.Sanitizer import Sanitizer


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
