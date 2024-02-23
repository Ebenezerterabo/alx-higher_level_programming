#!/usr/bin/python3

"""
This module appends a string at the end of a file and returns
the number of characters added.
"""


def append_write(filename="", text=""):
    """
    appends a string in a file and returns the number of characters.

    Args:
        filename (str): The name of the text file.
        text (str): The string appended in the file.

    Returns:
        int: The number of character
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)

    return len(text)
