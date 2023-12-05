#!/usr/bin/python3

"""Defines a file reading function."""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
