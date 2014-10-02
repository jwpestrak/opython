"""
Simple bunch class with a pretty printing method that protects its API.
"""

class Bunch(object):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                raise AttributeError("API conflict: '%s' is part of '%s' API" % 
                                     (key, self.__class__.__name__))
            else:
                setattr(self, key, value)

    def pretty(self):
        text = ""
        for key, value in self.__dict__.items():
            text += "%s: %s\n" % (key, value)
        return text
