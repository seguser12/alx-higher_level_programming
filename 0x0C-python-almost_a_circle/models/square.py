#!/usr/bin/python3
'''python square class module'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class that inherits from the Rectangle class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initializes the square method'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''overload rectangle str method'''
        return "[Square] ({}) {}/{} - {}".format(
                self.__id, self.__x, self.__y, self.__width)

    @property
    def size(self):
        '''gets the valeu of size'''
        return super().width

    @size.setter
    def size(self, value):
        '''sets the value of size'''
        __value = value
        super(Square, type(self)).width.fset(self, __value)

    def __str__(self):
        '''str magic method'''
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        '''update the square attributes'''
        attrs = ('id', 'size', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        '''returns dictionary representation of square'''
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
