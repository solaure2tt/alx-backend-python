#!/usr/bin/env python3
""" type-annotated function concat that takes a
    string str1 and a string str2 as arguments
    and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """concatenate two string
       Args:
           str1 (str): first string
           str2 (str): second string
       Return:
           concatenation of str1 and str2
    """
    return (str1 + str2)
