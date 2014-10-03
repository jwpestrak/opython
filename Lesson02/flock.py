from bird_api import Bird

class Flock(object):

    birds = []

    def add_bird(self, bird):
        """
        Add a bird object to the flock.
        """
        self.birds.append(bird)

    def race(self):
        """
        Show how far the flock birds can travel in an hour carrying their loads. 
        """
        print("Distance flown in one hour by the flock.")
        for bird in self.birds:
            distance = "-" * (bird.calculate() // 10)
            notice = "%s: %s carrying %s items" %
                     (distance, bird.name, len(bird.__dict__))
            print(notice)

if __name__ == "__main__":
    swallow = Bird(coconut = 1, 
                   name = 'Swallow')
    african = Bird(coconut = 1, 
                   piece = 'of string', 
                   visited = False,
                   name = 'African Swallow')
    european = Bird(coconut = 1, 
                    lottery_numbers = (23, 12, 34),
                    piece = 'of string',
                    visited = True, 
                    name = 'European Swallow')
    european.add('cereal boxes', 5)
    european.add('Norway', True)
    european.add('England', True)

    flock = Flock()
    flock.add_bird(swallow)
    flock.add_bird(african)
    flock.add_bird(european)
    flock.race()
