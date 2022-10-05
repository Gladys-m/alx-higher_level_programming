#!/usr/bin/python3
"""The first class base"""

class Base:
    """The base class of all other classes in the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects