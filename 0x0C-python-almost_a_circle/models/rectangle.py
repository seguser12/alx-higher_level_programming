#!/usr/bin/python3
'''rectangle class module'''

from models.base import Base


class Rectangle(Base):
    '''rectangle class that inherits from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor for rectangle class'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width getter method for rectangle class'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the value of width'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''height geeter method'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets value of height'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''x getter method'''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets value of x'''
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''gets value of y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets value of y'''
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''returns the area value of the rectangle'''
        area = self.__width * self.__height
        return area

    def display(self):
        '''prints in stdout the rectangle instance with #'''
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for column in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''assigns an args to each attribute'''
        if len(args) > 0:
            if len(args) > 0 and type(args[0]) == int:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'id' and isinstance(value, int):
                        self.id = value
                    if key == 'width':
                        self.width = value
                    if key == 'height':
                        self.height = value
                    if key == 'x':
                        self.x = value
                    if key == 'y':
                        self.y = value

    def to_dictionary(self):
        '''returns dictionary representation of rectangle class'''
        dict_rep = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
        return dict_rep
