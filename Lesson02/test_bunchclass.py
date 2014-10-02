"""
Tests for the Bunch class.
"""

import unittest
from bunchclass import Bunch

class TestBunch(unittest.TestCase):

    def test_pretty(self):
        self.assertRaises(AttributeError, Bunch, name="J", job="DS", pretty=True)
        b = Bunch(name="James", profession="Data Scientist")
        p = b.pretty()
        self.assertTrue("name: James" in p)
        self.assertFalse("pretty: True" in p)
        #self.assertEqual(len(p.splitlines()), 2, "Too many lines in output.")

if __name__ == "__main__":
    unittest.main()
