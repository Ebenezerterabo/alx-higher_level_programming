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
    def width(self, value):
        """Sets the width of the Rectangle"""
        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle"""
        self.__height = value

    @property
    def x(self):
        """Gets the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value"""
        self.__x = value

    @property
    def y(self):
        """Gets the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value"""
        self.__y = value
