#!/usr/bin/python3

""" Module rectangle """
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
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ Returns a readable string """
        return f"[Rectangle] {self.__width}/{self.__height}"
