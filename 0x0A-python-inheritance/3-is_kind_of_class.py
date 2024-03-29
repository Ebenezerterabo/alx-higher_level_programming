#!/usr/bin/python3

"""Module 3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance or class inherited

    Args:
    - obj: The object
    - a_class: The class

    Returns:
    - True if the objects is an instance, otherwise false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
