#!/usr/bin/python3

"""
This module returns the dictionary description with simple data structure
(list, dict, str, int and bool) for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Dictionary description with simple data structure for
    JSON serialization of an object.

    Args:
        obj (obj): An instance of a class

    Returns:
        obj (obj): An object
    """
    return obj.__dict__
