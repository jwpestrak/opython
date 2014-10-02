"""
Simple bunch class.
"""

class Bunch(object):
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    def pretty(self):
        text = ""
        for key, value in self.__dict__.items():
            text += "%s: %s\n" % (key, value)
        return text
