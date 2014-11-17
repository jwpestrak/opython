"""
composable.py: defines a composable function class
"""

import types

class Composable(object):

    def __init__(self, f):
        "Store function reference to proxied function."
        self.func = f

    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)

    def __mul__(self, other):
        "Return the composition of proxied and another function."
        if type(other) is Composable:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        raise TypeError("Illegal operands for multiplication.")

    def __pow__(self, p):
        "Return the pth composition of proxied function."
        if not isinstance(p, int):
            raise TypeError("Illegal type for exponentiation power")
        if p <= 0:
            raise ValueError("Illegal value for exponentiation power")
        f = Composable(self.func)
        while p > 1:
            p -= 1
            f *= Composable(self.func)
        return Composable(f)

    def __repr__(self):
        return "<Composable function {0} at 0x{1:X}>".format(self.func.__name__, id(self))
