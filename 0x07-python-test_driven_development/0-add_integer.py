#!/usr/bin/python3
"""Consists of a function that adds two integers"""

def add_integer(a, b=98):
    """Returns a + b typecasted as integers

    Raises a TypeError if a or b are not of type int or float"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
