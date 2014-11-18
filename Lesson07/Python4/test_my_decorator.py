import unittest
from my_decorator import addarg

class Test_my_decorator(unittest.TestCase):

    @addarg(1)
    def prargs(*args, **kwargs):
        return args, kwargs

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_int_only(self):
        self.assertEqual(self.prargs()[0][0], 1)

    def test_args_only(self):
        self.assertEqual(self.prargs(2, 3)[0][0], 1)
        self.assertEqual(self.prargs(2, 3)[0][2], 2)
        self.assertEqual(self.prargs(2, 3)[0][3], 3)

    def test_kwargs_only(self):
        self.assertEqual(self.prargs(dog='Duncan')[0][0], 1)
        self.assertEqual(self.prargs(dog='Duncan')[1], {'dog': 'Duncan'})

    def test_both(self):
        self.assertEqual(self.prargs(2, 3, dog='Duncan')[0][0], 1)
        self.assertEqual(self.prargs(2, 3)[0][2], 2)
        self.assertEqual(self.prargs(2, 3)[0][3], 3)
        self.assertEqual(self.prargs(dog='Duncan')[1], {'dog': 'Duncan'})

if __name__ == "__main__":
    unittest.main()
