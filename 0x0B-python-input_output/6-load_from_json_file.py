#!/usr/bin/python3

"""load_from_json_file function module."""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”:
    Args:
        filename: The file in which we should write
    Returns:
        Nothing.
    """
    with open(filename, encoding="utf-8") as myFile:
        return (json.load(myFile))
