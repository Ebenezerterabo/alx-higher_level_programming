#!/usr/bin/python3

"""A rectangle class"""


class Rectangle:
    """Initialize instance attributes"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter"""
        if self.__width and self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Generate a string representation of the rectangle"""
        pattern = ""

        if self.__width == 0 or self.__height == 0:
            return pattern

        for i in range(self.__height):
            row = "#" * self.__width
            pattern += row + "\n"
        return pattern

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
