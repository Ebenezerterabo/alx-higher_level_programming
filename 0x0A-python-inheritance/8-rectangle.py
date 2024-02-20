#!/usr/bin/python3
""" Module 8-rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class that models a Rectangle """
    def __init__(self, width, height):
        """
        Initializes an instance of a Rectangle object.

        Args:
        - width: The width of the rectangle
        - height: The height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
