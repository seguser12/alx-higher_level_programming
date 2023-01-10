#!/usr/bin/python3
'''working with python file input/output'''


def write_file(filename="", text=""):
    '''return no of characters written'''
    with open(filename, 'w', encoding='UTF-8') as f:
        write_file = f.write(text)
        return write_file
