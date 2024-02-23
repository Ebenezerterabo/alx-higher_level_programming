#!/usr/bin/python3

"""This module converts a python data structure to a JSON string"""
import json


def to_json_string(my_obj):
    """
    Converts python data structure to JSON string.

    Args:
        my_obj (obj): The data structure object

    Returns:
        str: JSON representation of an object
    """
    json_str = json.dumps(my_obj)
    return json_str
