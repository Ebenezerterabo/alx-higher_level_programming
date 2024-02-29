#!/usr/bin/python3
"""This module is a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the Square"""
        return self.width

    @size.setter
    def size(self, size_value):
        """Sets the size of the Square"""
        self.width = size_value
        self.height = size_value

    def __str__(self):
        """Returns the string in readable format"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
