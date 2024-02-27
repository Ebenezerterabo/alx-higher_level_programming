#!/usr/bin/python3

"""The module that contains a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        pass

    @width.setter
    def width(self, width):
        pass

    @property
    def height(self):
        pass

    @height.setter
    def height(self, height):
        pass

    @property
    def check_x(self):
        pass

    @check_x.setter
    def check_x(self, x):
        pass

    @property
    def check_y(self):
        pass

    @check_y.setter
    def check_y(self, y):
        pass
