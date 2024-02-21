#!/usr/bin/python3

"""A class MyList"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """A method that prints the list, but sorted"""
        print(sorted(self))
