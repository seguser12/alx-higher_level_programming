#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = tuple_a + (0, 0)
    second = tuple_b + (0, 0)
    new_tuple = first[0] + second[0], first[1] + second[1]
    return new_tuple
