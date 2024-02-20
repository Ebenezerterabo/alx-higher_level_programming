#!/usr/bin/python3

""" Module 2-is_same_class.py """


def is_same_class(obj, a_class):
    """
    A function that returns the instance of a specified class.


    Args:
    - obj: The object to perform the instance check on
    - a_class: The class


    Returns:
    - True, otherwise False
    """
    return type(obj) == a_class
