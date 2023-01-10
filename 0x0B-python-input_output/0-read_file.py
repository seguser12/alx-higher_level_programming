#!/usr/bin/python3
'''working with python input/output'''


def read_file(filename=""):
    with open(filename, encoding='UTF-8') as f:
        print(f.read())
