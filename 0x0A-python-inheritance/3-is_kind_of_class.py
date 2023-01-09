#!/usr/bin/python3
"""Defines a class checking function."""


def is_same_class(obj, a_class):
    '''checks if an object is an instance of class it inherits from
    args:
        obj: obj to check
        a_class: class that obj inherits from
    returs:
        true if object is an instance of class
    '''

    return True if isinstance(obj, a_class) else False
