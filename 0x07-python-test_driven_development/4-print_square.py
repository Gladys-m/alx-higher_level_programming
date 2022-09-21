#!/usr/bin/python3
"""Consists of a function that prints pattern with #"""

def print_square(size):
    """Prints a square using character #
    Size is the size of the square
    Raises:
        TypeError if size is not an int
        ValueError if size is less than 0
        TypeError if size is a float and less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")

        print()
