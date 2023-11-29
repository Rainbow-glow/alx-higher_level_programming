#!/usr/bin/python3
for a in range(9):
    for b in range(a + 1, 10):
        if a * 10 + b < 89:
            print("{:d}{:d}".format(a, b), end=", ")
print("{:d}".format(89))
