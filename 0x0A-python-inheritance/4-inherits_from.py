#!/usr/bin/python3

""" Module 4-ingerits_from.py """


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class inherited

    Args:
    - obj: The object
    - a_class: The class

    Returns:
    - True if the object is an instance of a class inherited, otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
