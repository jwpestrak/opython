"""
Simple bunch class.
"""

import unittest
from bunchclass import Bunch

class TestBunch(unittest.TestCase):

    def test_attributes(self):
        b = Bunch(name="Python 3", language="Python 3.4.1")
        self.assertEqual("Python 3", b.name)
        self.assertEqual("Python 3.4.1", b.language)

    def test_pretty(self):
        b = Bunch(name="James", profession="Data Scientist")
        self.assertTrue("name: James" in p)
        self.assertTrue("profession: Data Scientist" in p)
        self.assertEqual(len(p.splitlines()), 2, "Too many lines in output.")

if __name__ == "__main__":
    unittest.main()
