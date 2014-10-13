import re

class Address(object):

    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip_code = zip_code 

    def name(self):
        return self._name
    name = property(name)

    def street_address(self):
        return self._street_address
    street_address = property(street_address)

    def city(self):
        return self._city
    city = property(city)

    def state(self):
        return self._state
    def set_state(self, value):
        pat = re.compile("[A-Z]{2}")
        if not pat.search(value):
            raise StateError
        self._state = value
    state = property(state, set_state)

    def zip_code(self):
        return self._zip_code
    def set_zip_code(self, value):
        pat = re.compile("[0-9]{5}")
        if not pat.search(value):
            raise ZipCodeError
        self._zip_code = value
    state = property(zip_code, set_zip_code)


