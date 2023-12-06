#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_element = my_list[:]
    for x in range(len(new_element)):
        if new_element[x] == search:
            new_element[x] = replace
    return (new_element)
