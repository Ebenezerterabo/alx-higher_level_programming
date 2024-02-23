#!/usr/bin/python3

"""
This module is a class that defines student
"""


class Student:
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializing instance attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of a
        student instance.
        """
        return self.__dict__
