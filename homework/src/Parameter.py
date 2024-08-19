"""
TODO:

foo should accept an integer argument.
"""


def foo(x: int):
    if isinstance(x, int):
        print(f"параметр целочисленный: {x}")
    else:
        raise TypeError("печалька, но параметр не целочисленный")