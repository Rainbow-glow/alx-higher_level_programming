#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for r in range(4, 6):
            c = add(c, r)
        return (c)

    else:
        return(sub(a, b))
