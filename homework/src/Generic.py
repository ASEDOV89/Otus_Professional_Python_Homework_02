"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
"""

from typing import TypeVar, Protocol

class SupportsAdd(Protocol):
    def __add__(self, other: "SupportsAdd") -> "SupportsAdd":
        ...

T = TypeVar('T', bound=SupportsAdd)

def add(a: T, b: T) -> T:
    return a + b
