#!/usr/bin/python3

"""from_json_string function module."""
import json


def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string:
    Args:
        my_str (JSON): The JSON string to be converted to object.
    Returns:
        an object (Python data structure) represented by my_str (JSON string).
    """
    return json.loads(my_str)
