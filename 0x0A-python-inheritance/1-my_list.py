#!/usr/bin/python3
"""Defines a MyList class, inherited list class."""


class MyList(list):
    """prints the list, but sorted (ascending sort)"""

    def print_sorted(self):
        print(sorted(self))
