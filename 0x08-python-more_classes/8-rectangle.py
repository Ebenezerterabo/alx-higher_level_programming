#!/usr/bin/python3

"""A rectangle class"""


class Rectangle:
    """Public class attribute"""
    number_of_instances = 0
    print_symbol = "#"

    """Initialize instance attributes"""
    def __init__(self, width=0, height=0, print_symbol="#"):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            row = str(self.print_symbol) * self.__width
            pattern += row + "\n"
        pattern = pattern[:-1]
        return pattern

    def __repr__(self):
        """Generate string representation for developers"""
        return f"Rectangle{(self.__width, self.__height)}"

    def __del__(self):
        """Displayed message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the biggest
        rectangle base on the area

        Args:
         rect_1: rectangle_1
         rect_2: rectangle_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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
