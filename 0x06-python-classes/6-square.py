#!/usr/bin/python3
"""defines a square object"""


class Square:
    """Defines a square object
    Attibutes:
        __size(int): defines size of one side of the square
    """

    def __init__(self, size=0, position=0):
        """initializes an instance of a square
        Args:
            size: size of one side of the square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")


        if isinstance(position, tuple):
            if len(position) is not 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            elif position[0] is not > 0 and position[1] is not > 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    def position(self):
        return self.position

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        
        if isinstance(value, tuple):
            if len(value) is not 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            elif value[0] is not > 0 and value[1] is not > 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        areasize = self.__size * self.__size
        return areasize

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    if position[1] is < 0:
                        for i in range(position[0]):
                            print("_", end'')
                    print("#", end='')
                print()
