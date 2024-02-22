#!/usr/bin/python3

""" Base geometry class """


class BaseGeometry:
    """ A public method for area of geometry """

    def area(self):
        """ Raise exception not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ An integer validator method

        Args:
           name: Error name
           value: The value
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
