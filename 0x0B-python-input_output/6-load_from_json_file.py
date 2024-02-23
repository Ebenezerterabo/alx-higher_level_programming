#!/usr/bin/python3

"""This module creates an object from JSON file"""

import json


def load_from_json_file(filename):
    """
    Creates an object from JSON file..

    Args:
        filename (str): The filename

    Returns:
        obj: Object from a JSON file.
    """
    with open(filename, "r") as file:
        json_obj = json.load(file)

    return json_obj
