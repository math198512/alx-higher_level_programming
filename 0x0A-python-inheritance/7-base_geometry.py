#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """method to compute area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
