#!/usr/bin/python3


"""
A function that returns the instance of a specified class.


Args:
- obj: The object to perform the instance check on
- a_class: The class


Returns:
- True, otherwise False
"""


def is_same_class(obj, a_class):
    return type(obj) == a_class
