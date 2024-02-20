#!/usr/bin/python3

"""
Checks if an object is an instance or class inherited

Args:
- obj: The object
- a_class: The class

Returns:
- True if the objects is an instance, otherwise false
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
