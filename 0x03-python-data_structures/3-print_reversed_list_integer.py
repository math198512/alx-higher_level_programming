#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """"prints all integers of a list, in reverse order"""
    if not my_list:
        pass
    else:
        rev = range(len(my_list) - 1,  -1, -1)
        for i in rev:
            print("{:d}".format(my_list[i]))
