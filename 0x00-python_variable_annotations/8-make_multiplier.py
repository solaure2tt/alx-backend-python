#!/usr/bin/env python3
""" type-annotated function make_multiplier that takes
    a float multiplier as argument and returns a
    function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that multiplies a float by multiplier
       Args:
        multiplier (float): number to multiply
       Returns:
        A function that multiplies a float by multiplier
    """
    def multiplier_fun(number: float) -> float:
        """Multiplies a float by multiplier"""
        return multiplier * number

    return multiplier_fun
