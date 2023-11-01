#!/usr/bin/python3
def uppercase(str):
    buff = ""
    for i in range(len(str)):
        c = str[i]
        if ord(c) > 96 and ord(c) < 123:
            c = chr(ord(c) - 32)
        buff += c
    print("{}".format(buff))
