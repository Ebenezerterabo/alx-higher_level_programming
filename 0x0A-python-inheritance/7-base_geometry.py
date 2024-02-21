#!/usr/bin/python3

""" Base geometry class """


class BaseGeometry:
    """ A public method for area of geometry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ An integer validator method """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
