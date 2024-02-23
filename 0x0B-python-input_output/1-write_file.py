#!/usr/bin/python3

"""
This module writes a string in a file and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string in a file and returns the number of characters.

    Args:
        filename (str): The name of the text file.
        text (str): The string written in the file.

    Returns:
        int: The number of character
    """
    with open(filename, "w", encoding="utf-8") as file:
        count = 0

        for i in range(len(text)):
            if text[i] != '':
                count += 1

        return count
