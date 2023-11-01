#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = str[i]
        if ord(c) > 96 and ord(c) < 123:
            str[i] = chr(ord(c) - 32)
    print("{}".format(str))
