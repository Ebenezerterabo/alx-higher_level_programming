#!/usr/bin/python3

"""
This module returns a python data structure represented
by JSON string
"""
import json


def from_json_string(my_str):
    """
    converts JSON string to python data structure.

    Args:
        my_str (str): The json string

    Returns:
        obj: python data structure
    """
    data_obj = json.loads(my_str)
    return data_obj
