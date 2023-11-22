#!/usr/bin/python3
"""class Square that defines a square"""


class Square():
    """square class with it's size and proper validation"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, value):
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of two \
                    positive integers")
        self.__position = value

    def area(self):

        return (self.__size * self.__size)

    def my_print(self):
        size = self.__size
        if size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(size):
                print(" " * self.__position[0], end="")
                for j in range(size):
                    print("#", end="")
                print()
