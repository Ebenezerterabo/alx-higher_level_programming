#!/usr/bin/python3

"""
A class that defines a square
"""


class Square:
    """initialize the class instance

    Args:
       size: integer
    """
    def __init__(self, size=0):
        """
        define attribute of instance
        """
        self.__size = size

        """validating size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
