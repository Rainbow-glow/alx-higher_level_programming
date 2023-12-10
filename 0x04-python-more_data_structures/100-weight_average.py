#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg = 0
    size = 0
    for tuples in my_list:
        avg = avg + (tuples[0] * tuples[1])
        size = size + tuples[1]
        return (avg / size)
