#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score = 0
    key_max_score = ''
    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            key_max_score = key
    return key_max_score
