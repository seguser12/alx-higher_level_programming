#!/usr/bin/python3
'''unittest for rectangle class'''

import unittest
import io
import contextlib
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''testing the rectangle class'''
    def test_id(self):
        '''testing if id attribute is properly set'''
        r1 = Rectangle(10, 2)

        r2 = Rectangle(2, 5)
        self.assertEqual(r2.id, r1.id + 1)

        r3 = Rectangle(10, 20, 4, 0, 9)
        self.assertEqual(r3.id, 9)

    def test_no_of_argumnet(self):
        '''Test to see that arguments are properly supplied'''
        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(8)

    def test_validation(self):
        'Test to check if type of argument is correct'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle('4', 43)

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 39)

        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(3, 0)

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(3, 'mitche')

        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(4, 3, -1, 2)

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(93, 3, '')

        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(9, 3, 3, -48)

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(8, 39, 92, '')

    def test_area(self):
        '''test if area method of rectangle has been correctly implemented'''
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

        r1 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 20)

        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

        r2.width = 7
        r2.height = 14
        self.assertEqual(r2.area(), 98)

        with self.assertRaises(TypeError):
            r.area(6)

    def test_display(self):
        '''test for display method to check its properly implemented'''
        r1 = Rectangle(4, 6)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        result = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(s, result)

        with self.assertRaises(TypeError):
            r1.display(9)

        i = io.StringIO()
        r2 = Rectangle(2, 3, 2, 2)
        with contextlib.redirect_stdout(i):
            r2.display()
        s = i.getvalue()
        result = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, result)

    def test_str_(self):
        ''' test the _str_ magic method'''
        f = io.StringIO()
        r1 = Rectangle(4, 6, 2, 1, 12)
        with contextlib.redirect_stdout(f):
            print(r1)
        s = f.getvalue()
        result = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(s, result)

    def test_update(self):
        '''test the update method of rectangle'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(2, 3, 7, 9, 34)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 34)

        r2 = Rectangle(1, 3, 5, 8)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r2.update(3, 'hi')
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r2.update(4, 8, '7')
        r2.update(height=10, x=7, y=8, width=16)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r2.y, 8)
        self.assertEqual(r2.width, 16)

    def test_to_dictionary(self):
        """Test for the method to_dictionary"""
        rect = Rectangle(10, 20, 30, 40)
        rect_dict = rect.to_dictionary()
        rect_dict1 = {
                'x': 30,
                'y': 40,
                'id': 1,
                'height': 20,
                'width': 10
                }
        self.assertEqual(len(rect_dict), len(rect_dict1))
        self.assertEqual(type(rect_dict), dict)
        rect2 = Rectangle(12, 22)
        rect2.update(**rect_dict)
        rect_dict2 = rect2.to_dictionary()
        self.assertEqual(len(rect_dict), len(rect_dict2))
        self.assertEqual(type(rect_dict2), dict)
        self.assertFalse(rect == rect2)

        mes = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 20, 30, 40)
            r.to_dictionary("3")
        self.assertEqual(mes, str(e.exception))
