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
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of a Rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints the structure of the Rectangle"""
        for _ in range(self.__height):
            print("#" * self.__width)
