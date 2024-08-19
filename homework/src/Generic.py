"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
"""

from typing import TypeVar

T = TypeVar('T', bound=int)

def add(a: T, b: T) -> T:
    return a + b