#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    if not a_dictionary:
        return None
    key2 = max(a_dictionary, key=lambda k: a_dictionary[k])
    return (key2)
