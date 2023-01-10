#!/usr/bin/python3
'''working with python input/output'''

import json


def load_from_json_file(filename):
    '''creates an object from json file'''
    with open(filename) as f:
        return json.load(f)
