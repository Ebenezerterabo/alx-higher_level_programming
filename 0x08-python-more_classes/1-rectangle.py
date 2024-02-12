#!/usr/bin/python3

"""A rectangle that defines a rectangle"""


class Rectangle:
    """Initialize instance attributes"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve and return the value and width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value width"""
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retrieve and return the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height"""
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
