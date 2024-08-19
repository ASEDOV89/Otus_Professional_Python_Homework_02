"""
TODO:

foo should accept a tuple argument, 1st item is a string, 2nd item is an integer.
"""


def foo(x: tuple[str, int]):
    if isinstance(x[0], str) and isinstance(x[1], int):
        pass
    else:
        raise ValueError("первый аргумент должен быль строковым, а второй целочисленным")