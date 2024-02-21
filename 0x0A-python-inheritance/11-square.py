#!/usr/bin/python3
""" Base geometry class """


class BaseGeometry:
    """ A public method for area of geometry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ An integer validator method """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")



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
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
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
