#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    biggest = a_dictionary[ret]
    for a, b in a_dictionary.items():
        if b > biggest:
            biggest = b
            ret = a

    return (ret)
