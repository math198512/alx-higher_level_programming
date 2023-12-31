#!/usr/bin/python3

"""Defines a file writing function."""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns
    the number of characters written
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return (myFile.write(text))
