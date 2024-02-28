#!/usr/bin/python3

"""The module that contains a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle

        Args:
           width (int): The width of the rectangle
           height (int): The height of the rectangle
           x (int) : The x cordinate of the rectangle
           y (int) : The y cordiante of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, val):
        """Sets the width of the Rectangle"""
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")

        self.__width = val

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, val):
        """Sets the height of the Rectangle"""
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")

        self.__height = val

    @property
    def x(self):
        """Gets the x value"""
        return self.__x

    @x.setter
    def x(self, val):
        """Sets the x value"""
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")

        self.__x = val

    @property
    def y(self):
        """Gets the y value"""
        return self.__y

    @y.setter
    def y(self, val):
        """Sets the y value"""
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")

        self.__y = val
