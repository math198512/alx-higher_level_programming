#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element in a list without modifying the original list"""
    if not my_list:
        pass
    else:
        new_list = len(my_list) * [0]
        for i in range(len(my_list)):
            new_list[i] = my_list[i]
        if idx < 0 or idx > len(my_list) - 1:
            return (new_list)
        else:
            new_list[idx] = element
            return (new_list)
