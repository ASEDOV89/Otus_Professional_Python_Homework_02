"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""


from typing import Callable, TypeVar

F = TypeVar('F', bound=Callable)

def decorator(func: F) -> F:
    return func