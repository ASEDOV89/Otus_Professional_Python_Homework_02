"""
TODO:

`foo` takes keyword arguments of type integer or string.
"""


def foo(**kwargs: int | str):
    for key, value in kwargs.items():
        if isinstance(value, (int, str)):
            print(f"{key}: {value}")
        else:
            raise ValueError("аргументы должны быть либо целые числа, либо строковые")

