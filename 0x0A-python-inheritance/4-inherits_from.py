#!/usr/bin/python3

"""Defines a function to check the subclasses of an object."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of the subclasses of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance of the subclasses of a_class - True.
        Otherwise - False.
    """

    if (type(obj) is not a_class):
        return (issubclass(type(obj), a_class))
    return (False)
