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

        """ Validate size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Getter method for the size attribute """
        return self.__size ** 2
