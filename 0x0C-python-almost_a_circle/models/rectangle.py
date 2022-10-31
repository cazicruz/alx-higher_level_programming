#!/usr/bin/python3
""" a child class that inherits from a parent class Base """
from models.base import Base

class Rectangle(Base):
    """ Rectangle representation """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization of the class Rectangle"""

        self.width = width
        self.heightb= height
        self.x = x
        self.y = y
        super.__init__(id)

    @property
    def width(self):
        """ get the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """" Sets the value of width"""
        self.__width = value

     @property
    def height(self):
        """ get the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """" Sets the value of height """
        self.__height = value


 @property
    def x(self):
        """ get x of the rectangle"""

        return self.__x

    @x.setter
    def x(self, value):
        """" Sets the value of x"""
        self.__x = value

     @property
    def y(self):
        """ get y of the rectangle"""

        return self.__y

    @y.setter
    def y(self, value):
        """" Sets the value of y"""
        self.__y = value
