#!/usr/bin/python3

"""A class MyList"""


class MyList(list):
    def print_sorted(self):
        """A method that prints the list, but sorted"""
        print(sorted(self))
