#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    keys = list(new_dict.keys())

    for j in keys:
        new_dict[j] *= 2

    return (new_dict)
