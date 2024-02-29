#!/usr/bin/python3
"""This module is a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self._size = size

    @property
    def size(self):
        """Gets the size of the Square"""
        return self._size

    @size.setter
    def size(self, size_value):
        """Sets the size of the Square"""
        if type(size_value) != int:
            raise TypeError("width must be an integer")
        elif size_value <= 0:
            raise ValueError("width must be > 0")
        self._size = size_value

    def __str__(self):
        """Returns the string in readable format"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self._size}"
