"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
The decorator takes an argument `message` of type string
"""


from typing import TypeVar, Callable, Any

T = TypeVar('T')

def decorator(func: Callable[..., T]) -> Callable[..., T]:
    def wrapper(*args: Any, **kwargs: Any) -> T:
        return func(*args, **kwargs)
    return wrapper

# from typing import TypeVar
# from collections.abc import Callable
#
# def decorator[T: Callable](message:str) -> Callable[[T], T]:
#     ...