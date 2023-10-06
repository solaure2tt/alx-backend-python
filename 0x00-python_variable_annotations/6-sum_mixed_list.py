#!/usr/bin/env python3
"""  type-annotated function sum_mixed_list which
     takes a list mxd_lst of integers and floats
     and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """fuction that return the sum of a list of floats and ints
       Args:
        mxd_lst (list): A list of floats and ints
       Returns:
        float: The sum of the floats in the list"""
    if mxd_lst is None:
        return 0
    return sum(mxd_lst)
