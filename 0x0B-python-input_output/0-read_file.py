#!/usr/bin/python3
'''working with python input/output'''


def read_file(filename=""):
    '''reads a text file and prints it to stdout'''
    with open(filename, encoding='UTF-8') as f:
        print(f.read())
