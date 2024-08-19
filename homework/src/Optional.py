"""
TODO:

foo can accept an integer argument, None or no argument at all.
"""


def foo(x: int | None = 0):
    if x is None:
        print("нет аргументов")
    elif isinstance(x, int):
        print(f"целочисленное: {x}")
    else:
        raise TypeError("аргумент не является целочисленным или отсутствующим")