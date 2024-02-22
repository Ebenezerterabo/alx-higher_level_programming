#!/usr/bin/python3

""" Module square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Initialize method """
    def __init__(self, size):
        """
        Initializes an instance of a square

        Args:
           size: size of the square
        """
        self.__size = size

        self.integer_validator("size", size)

    def area(self):
        """Area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """ Return a readable string """
        return f"[Square] {self.__size}/{self.__size}"
