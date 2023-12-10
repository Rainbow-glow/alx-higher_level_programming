#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)
    roman_fig = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    val = 0

    for i in range(len(roman_string)):
        if roman_fig.get(roman_string[i], 0) == 0:
            return (0)
        if (i != (len(roman_string) - 1) and
                roman_fig[roman_string[i]] < roman_fig[roman_string[i + 1]]):
            val = val + roman_fig[roman_string[i]] * -1

        else:
            val = val + roman_fig[roman_string[i]]
    return (val)
