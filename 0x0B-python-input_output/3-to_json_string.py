#!/usr/bin/python3

"""to_json_string function module."""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string):
    Args:
        my_obj (str): The string to be represented as JSON.
    Returns:
         the JSON representation of my_obj.
    """
    return json.dumps(my_obj)
