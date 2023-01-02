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

    def area(self):
        '''instance method that returns the area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''returns the perimeter of a rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = (self.__width + self.__height) * 2
        return perimeter

    def __str__(self):
        '''returns str representation'''
        if self.__width == 0 or self.__height == 0:
            return ''
        str_rep = ''
        for i in range(self.__height):
            for j in range(self.__width):
                str_rep += '#'
            str_rep += '\n'
        return str_rep[:-1]

    def __repr__(self):
        '''returns string reperesentation of rectangle instance'''
        return "Rectangle({}, {})".format(self.__width, self.__height)
