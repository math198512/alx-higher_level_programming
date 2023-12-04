#!/usr/bin/python3

"""Defines a function to check the class(or parent) of an object."""

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a given class or its parent.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class or its parent - True.
        Otherwise - False.
    """

    return(isinstance(obj, a_class))
