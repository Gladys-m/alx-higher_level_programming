#!/usr/bin/python3

"""consists of a function that determines if an obj is an instance of or instance
of class that it inheritted from"""

def is_kind_of_class(obj, a_class):
    """returns true if obj is an instance of a_class or inheritance"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
