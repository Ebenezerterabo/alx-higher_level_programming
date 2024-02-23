#!/usr/bin/python3


def read_file(filename=""):
    """
    Read a text file and prints it content.

    Args:
        filename (str): The name of the text file.
    """
    with open("my_file_0.txt") as file:
        content = file.read()
        print(content)
