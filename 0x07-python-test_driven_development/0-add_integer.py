#!/usr/bin/python3
"""
This function, add_integer(),
adds together 2 int or float types and returns an int.
"""


def add_integer(a, b=98):

    """Return the sum of two integers or floats as an integer.
    Otherwise raise a TypeError for given incorrect argument type.
    Usage:
    >>> add_integer(15, 0)
    15
    >>> add_integer(0, 15)
    15
    >>> add_integer(-2, 2)
    0
    >>> add_integer(2, -2)
    0
    >>> add_integer(2)
    100
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
