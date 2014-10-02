"""
Simple bunch class.
"""

class Bunch(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

if __name__ == "__main__":
    b = Bunch(name="Python 3", language="Python 3.4.1")
    print(b.name)
    print(b.language)
    print(b.__dict__)
