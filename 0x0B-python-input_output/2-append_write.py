#!/usr/bin/python3

"""Defines a file appending function."""


def append_write(filename="", text=""):
    """
    appends a string to a text file (UTF8) and returns
    the number of characters written
    Args:
        filename (str): The name of the file to write.
        text (str): The text to be appended to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return (myFile.write(text))
