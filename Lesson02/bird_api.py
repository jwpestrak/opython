"""
API for software birds carrying objects.
"""

from bunchclass import Bunch

class Bird(Bunch):

    def add(self, name, value):
        """
        Add an object for the Bird to carry in its basket.
            Name is a string naming the object.
            Value is the actual object being placed in the basket.
        """

    def remove(self, name):
        """
        Remove an object from the basket.
            Name is the string of the object to be removed.
        """

    def calculate(self):
        """
        Calculate the speed of the bird.
            algorithm: 100 - (5 * number of objects in basket)
            result cannot be less than zero
        """

    def basket(self):
        """
        Print in an attractive format the list of objects in the basket.
        """

if __name__ == "__main__":
    swallow = Bird(fruit = ("coconut", "orange"), drink = "apple juice")
    swallow.add("cars", 3)
    print(swallow.basket())
    print(swallow.calculate())
    swallow.remove("drink")
    print(swallow.basket())
    print(swallow.calculate())
    help(swallow)
