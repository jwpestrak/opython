"""
Test functionality of map_the_home() function.
"""

import unittest
from furnishings import *

class Test_furnishings(unittest.TestCase):

    def test_map_the_home(self):
        home = [
               Sofa('Living Room'),
               Bookshelf('Living Room'),
               Table('Living Room'),
               Bookshelf('Bedroom'),
               Table('Bedroom'),
               Bed('Bedroom')
               ]
        tdct = map_the_home(home)
        self.assertIsInstance(tdct, dict)
        self.assertEqual(set(tdct.keys()), set(['Living Room', 'Bedroom']))
        self.assertIsInstance(tdct['Living Room'][0], Sofa)
        self.assertIsInstance(tdct['Living Room'][1], Bookshelf)
        self.assertIsInstance(tdct['Living Room'][2], Table)
        self.assertIsInstance(tdct['Bedroom'][0], Bookshelf)
        self.assertIsInstance(tdct['Bedroom'][1], Table)
        self.assertIsInstance(tdct['Bedroom'][2], Bed)

if __name__ == '__main__':
    unittest.main()
