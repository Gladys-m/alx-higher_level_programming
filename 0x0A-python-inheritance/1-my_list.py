#!/usr/bin/python3
"""consists of a class that inherits from list"""

class MyList(list):
    """creates an instance of the class to use super function"""
    def __init__(self):
        super().__init__()

    """the method that prints the sorted list"""
    def print_sorted(self):
        print(sorted(self))
