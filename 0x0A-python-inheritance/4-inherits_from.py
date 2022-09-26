#!/usr/bin/python3

"""consists of a function that checks if obj is instance of class inherited directly of indirectly"""

def inherits_from(obj, a_class):
    """returns true if obj is instance of class else false"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
