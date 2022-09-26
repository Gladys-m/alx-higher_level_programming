#!/usr/bin/python3

"""consists of a function that determines if obj is an instance of a class"""

def is_same_class(obj, a_class):
    """returns true if obj is of type class else false"""
    
    if type(obj) == a_class:
        return True
    else:
        return False
