#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    # second par is optional.
    # A value to return if the specified key do not exist.
    return (a_dictionary)
