#!/usr/bin/python3

"""The module that contains a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
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
    def width(self, width):
        """Sets the width of the Rectangle"""
        self.__width = width

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the Rectangle"""
        self.__height = height

    @property
    def x(self):
        """Gets the x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x value"""
        self.__x = x

    @property
    def y(self):
        """Gets the y value"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y value"""
        self.__y = y
