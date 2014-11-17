"""
test_composable.py: performs simple tests of composable functions
"""

import unittest
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing."
    return s[::-1]

def square(x):
    "Multiplies a number by itself."
    return x * x

class ComposableTestCase(unittest.TestCase):

    def test_inverse(self):
        "The purpose of this test is to ensure that s = reverse(reverse(s))."

        reverser = Composable(reverse)
        nulltran = reverser ** 2
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEquals(nulltran(s), s)

    def test_square(self):
        "The purpose of this test is to ensure that square(x) = x * x."

        squarer = Composable(square)
        po4 = squarer * squarer
        for v, r in ((1, 1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)

    def test_exceptions(self):
        """
        The purpose of this test is to ensure that passing
        (1) a non-Composable object to the __mul__ method raises a TypeError and
        (2) a non-integer argument to the __pow__ method raises a TypeError and
        (3) a non-positive argument to the __pow__ method raises a ValueError.
        """

        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc ** q
        with self.assertRaises(ValueError):
            fc ** -1

if __name__ == '__main__':
     unittest.main()
