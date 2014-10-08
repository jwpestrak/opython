
class Centipede(object):
    
    def __init__(self):
        self.stomach = []
        self.legs = []

    def __call__(self, arg):
        #for arg in args:
        self.stomach.append(arg)
    
    #def __setattr__(self, key, value):
    #    self.__dict__[key] = value
    #    self.legs.append(key)
 
    def __str__(self):
        print(','.join(self.stomach))

    def __repr__(self):
        return 'asdf' 
