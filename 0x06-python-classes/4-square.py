#!/usr/bin/python3
""" square definition """


class Square:
    '''square class'''
    def __init__(self, size=0):
        '''class initialization
        Args:
            size: size o the square
        '''
        self.__size = size

    @property
    def size(self):
        '''get current size of square'''
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''instance method that returns current square area'''
        return self.__size ** 2
