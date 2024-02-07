#!/usr/bin/python3

"""
A class that defines a square.
"""


class Square:
    """
    Initializing the instance of a class

    Args:
       size: integer
    """
    def __init__(self, size=0):
        """initializing attribute of an instance """
        self.__size = size

    @property
    def size(self):
        """setter method for the size attribute """
        return self.__size

    @size.setter
    def size(self, size):
        """Getter method for the size attribute """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ returnt the current square area """
        return self.__size ** 2
