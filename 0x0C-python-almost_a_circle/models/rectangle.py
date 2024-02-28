#!/usr/bin/python3
"""
The module that contains a Rectangle class
"""


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
    def width(self, width_value):
        """Sets the width of the Rectangle"""
        if type(width_value) != int:
            raise TypeError("width must be an integer")
        elif width_value <= 0:
            raise ValueError("width must be > 0")
        self.__width = width_value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, height_value):
        """Sets the height of the Rectangle"""
        if type(height_value) != int:
            raise TypeError("height must be an integer")
        elif height_value <= 0:
            raise ValueError("height must be > 0")
        self.__height = height_value

    @property
    def x(self):
        """Gets the x value"""
        return self.__x

    @x.setter
    def x(self, x_value):
        """Sets the x value"""
        if type(x_value) != int:
            raise TypeError("x must be an integer")
        elif x_value < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_value

    @property
    def y(self):
        """Gets the y value"""
        return self.__y

    @y.setter
    def y(self, y_value):
        """Sets the y value"""
        if type(y_value) != int:
            raise TypeError("y must be an integer")
        elif y_value < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_value

    def area(self):
        """Area of a Rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints the structure of the Rectangle"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Return the readable string to the user"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                f" - {self.__width}/{self.__height}")

    def update(self, *args):
        """Assigns args to each attribute.

        Args:
           id (int): 1st argument
           width (int): 2nd argument
           height (int): 3rd argument
           x (int): 4th argument
           y (int): 5th argument
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
