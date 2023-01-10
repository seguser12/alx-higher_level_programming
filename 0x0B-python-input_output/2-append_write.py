#!/usr/bin/python3
'''working with python input/output'''


def append_write(filename='', text=''):
    '''appends a string at the end of a text file'''
    with open(filename, 'a', encoding='UTF-8') as f:
        write_file = f.write(text)
        return write_file
