#!/usr/bin/python3
"""This module is a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the attribute

        Args:
           size (int): The size of the square
           x (int): The x-cordinate of the square
           y (int): The y-cordinate of the square
           id (int): The square identifier
        """
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

    def update(self, *args, **kwargs):
        """This method update the attributes

        Args:
           id (int): 1st argument
           size (int): 2nd argument
           x (int): 3rd argument
           y (int): 4th argument
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns the string in readable format"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
