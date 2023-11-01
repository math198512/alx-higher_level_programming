#!/usr/bin/python3
listOrig = range(97, 123)
rev = range(max(listOrig), min(listOrig) - 1, -1)
for x in rev:
    temp = x
    if x % 2 == 1:
        temp = x - 32
    print("{}".format(chr(temp)), end="")
