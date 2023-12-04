#!/usr/bin/python3
'''Module for Rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rctangle (subclass) definition"""
    def __init__(self, width, height):
        '''Constructor.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):

        """string representation of a Rectangle."""
        x = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return (x)

    def __repr__(self):

        """Return the string representation of the Rectangle."""
        x = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return (x)

    def area(self):

        """compuctes are of rectangle"""
        return (self.__width * self.__height)
