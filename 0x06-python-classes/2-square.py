#!/usr/bin/python3
""" square definition """


class Square:
    '''square class'''
    def __init__(self, size=0):
        '''class initialization
        Args:
            size: size o the square
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
