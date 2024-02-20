#!/usr/bin/python3

""" A module that returns the list of available attributes and methods
of an object
"""


def lookup(obj):
    """
    Perform a lookup operation on the given object.

    Args:
    - obj: The object to perform the lookup operation on.

    Returns:
    - list: The result of the lookup operation.
    """
    return dir(obj)
