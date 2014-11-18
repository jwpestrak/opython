class Tree(object):

    def __init__(self, key, value):
        "Create a new Tree object with empty L & R subtrees."
        self.key = key
        self.left = self.right = None

    def insert(self, key, value):
        "Insert a new element into the tree in the correct position."
        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = Tree(key, value)
        elif key > self.key:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = Tree(key, value)
        else:
            raise ValueError("Attempt to insert duplicate value")

    def walk(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n in self.left.walk():
                yield n
        yield self.key
        if self.right:
            for n in self.right.walk():
                yield n
                
    def find(self, key):
        "Find a specified key and return its value."
        if key < self.key:
            if self.left:
                return self.left.find(key)
            else:
                raise KeyError("Key not found!")
        elif key > self.key:
            if self.right:
                return self.right.find(key)
            else:
                raise KeyError("Key not found!")
        else:
            return self.value
