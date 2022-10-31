#!/usr/bin/python3
""" Define a class Base"""

class Base:
    """represents the Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initiallization of the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = base.__nb_objects

