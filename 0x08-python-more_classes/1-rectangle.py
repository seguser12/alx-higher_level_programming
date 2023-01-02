#!/usr/bin/python3
'''A rectangle module'''


class Rectangle:
    '''a class that defines the rectangle'''
    def __init__(self, width=0, height=0):
        '''instance method to initialize rectangle class
        args:
            width: width of rectangle
            height: height of the rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''retrieves and returns the value of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the value of width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''retrives the value of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the value of height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
