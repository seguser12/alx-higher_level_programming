#!/usr/bin/python3
'''working with python input/output'''

import json


def class_to_json(obj):
    '''return dict description for json serialization of an obj'''
    return obj.__dict__
