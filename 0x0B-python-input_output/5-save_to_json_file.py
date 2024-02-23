#!/usr/bin/python3

"""
This module writes an object to a text file
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using
    JSON representation.

    Args:
        my_obj (obj): The object data structure
        filename (str): The filename
    """
    with open(filename, "w") as file:
        json_str = json.dumps(my_obj)
        file.write(json_str)
