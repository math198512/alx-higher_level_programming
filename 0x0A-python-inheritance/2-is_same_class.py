#!/usr/bin/python3

"""Defines a function to check the class of an object."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """

    return (type(obj) is a_class)
