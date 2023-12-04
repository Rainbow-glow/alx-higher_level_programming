#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divisor = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divisor.append(True)
        else:
            divisor.append(False)

    return (divisor)
