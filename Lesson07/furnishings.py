class Furnishing(object):
    "Base class for specific furniture classes."

    count = 0
    def __init__(self, room):
        self.room = room

class Sofa(Furnishing):

    def __init__(self, room):
        Furnishing.__init__(self, room)
        Sofa.count += 1 

class Bookshelf(Furnishing):

    def __init__(self, room):
        Furnishing.__init__(self, room)
        Bookshelf.count += 1

class Bed(Furnishing):

    def __init__(self, room):
        Furnishing.__init__(self, room)
        Bed.count += 1

class Table(Furnishing):

    def __init__(self, room):
        Furnishing.__init__(self, room)
        Table.count += 1

def map_the_home(hlst):
    """
    Convert list of Furnishing subclass instances to a dict where rooms are the 
    keys and their associated value is a list of furniture for that room.
    """

    hdct = {}
    for e in hlst:
        if e.room in hdct.keys():
            hdct[e.room].append(e)
        else:
            hdct[e.room] = [e]
    return hdct

def counter(flst):
    """
    Print the types of furniture in the home and associated counts.
    """

    fdct = {
           'Sofa': 0,
           'Bookshelf': 0,
           'Bed': 0,
           'Table': 0
           }
    for f in flst:
        if f.__class__.__name__ in fdct.keys():
            fdct[f.__class__.__name__] += 1
    return fdct
