#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if not my_list:
        return my_list
    for val in my_list:
        if val != search:
            new_list.append(val)
        else:
            new_list.append(replace)
    return (new_list)
