#!/usr/bin/env python3
"""  type-annotated function to_kv that takes a string k
     and an int OR float v as arguments and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """fuction that return the string k and the square of v
       Args:
        k (string): string to return
        v (int or float): int or float parameter
       Returns:
        tuple(str, float): The tuple (k, square(v))"""
    res = (k, v ** 2)
    return res
