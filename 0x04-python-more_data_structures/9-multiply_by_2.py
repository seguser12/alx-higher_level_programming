#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for keys, values in new_dict.items():
        values *= 2
        new_dict[keys] = values
    return new_dict
