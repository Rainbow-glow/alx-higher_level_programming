#!/usr/bin/python3

def uppercase(str):
    """prints a string in uppercase followed by a new line."""
    for i in str:
        if ord("a") <= ord(i) <= ord("z"):
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print()
