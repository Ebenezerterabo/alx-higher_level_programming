#!/usr/bin/python3

"""
A class square that defines a square
"""


class Square:
    """
    private instance of size
    """
    def __init__(self, size):
        """initialize a new instance.

        Args:
            size (int): the size of the square.
        """
        self.__size = size
