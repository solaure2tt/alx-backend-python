#!/usr/bin/env python3
""" Annotate the below function’s parameters
    and return values with the appropriate types
"""
from typing import Mapping, Optional, TypeVar, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """ value for a key in a dict
    """
    if key in dct:
        return dct[key]
    else:
        return default
