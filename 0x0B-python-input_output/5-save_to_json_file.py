#!/usr/bin/python3

"""save_to_json_file function module."""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation:
    Args:
        my_obj: The python object to be written into the file <filename>
        filename: The file in which we should write
    Returns:
        Nothing.
    """
    
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
    
