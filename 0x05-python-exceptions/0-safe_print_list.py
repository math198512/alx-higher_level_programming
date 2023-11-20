#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        else:
            counter = counter + 1
    print()
    return (counter)
