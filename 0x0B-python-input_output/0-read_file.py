#!/usr/bin/python3

"""This module reads and display the content of a file"""


def read_file(filename=""):
    """
    Read a text file and prints it content.

    Args:
        filename (str): The name of the text file.
    """
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content, end='')
