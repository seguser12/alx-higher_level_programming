#!/usr/bin/python3
'''test module for square class'''

import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class SquareTests(unittest.TestCase):
    '''unittest for Square class'''
    def test_inheritance(self):
        '''test for inheritance'''
        s = Square(1)
        self.assertIsInstance(s, Base)
        self.assertIsInstance(s, Rectangle)

    def test_no_of_args(self):
        '''test square with different args'''
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

        s = Square(10)
        s1 = Square(10, 2)
        s2 = Square(10, 2, 2, 8)
        self.assertEqual(s1.id, s.id + 1)
        self.assertEqual(10, s1.size)
        self.assertEqual(10, s2.width)
        self.assertEqual(2, s2.x)
        self.assertEqual(2, s2.y)
        self.assertEqual(8, s2.id)

    def test_validation(self):
        '''test if square is properly validated'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square("hi")

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(3.0)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square([83])

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(range(3))

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(0)

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(-2)

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, None)

        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(2, -3, 8)

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 2, '3')

        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Square(2, 3, -8)

    def test_str_(self):
        '''tests the _str_ square method'''
        self.assertEqual(
            str(Square(4, 0, 0, 1)),
            '[Square] (1) 0/0 - 4'
        )
        self.assertEqual(
            str(Square(4, 7, 12, 2)),
            '[Square] (2) 7/12 - 4'
        )
        self.assertEqual(
            str(Square(4, 4, 4, 3)),
            '[Square] (3) 4/4 - 4'
        )
        self.assertEqual(
            str(Square(4, 4, 4, 3.4)),
            '[Square] (3.4) 4/4 - 4'
        )
        self.assertEqual(
            str(Square(4, 2, 5, (4, 4))),
            '[Square] ((4, 4)) 2/5 - 4'
        )

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        correct = {
                'id': 1,
                'x': 2,
                'size': 10,
                'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)
