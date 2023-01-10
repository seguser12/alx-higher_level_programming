#!/usr/bin/python3
'''working with python input/output'''

import json


def from_json_string(my_str):
    '''returns an obj represented by a json string'''
    return json.loads(my_str)
