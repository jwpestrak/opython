import re

class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass

class Address(object):

    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip_code = zip_code 

    def name(self):
        return self._name
    def set_name(self, value):
        raise AttributeError
    def del_name(self):
        raise AttributeError
    name = property(name, set_name, del_name)

    def street_address(self):
        return self._street_address
    def set_street_address(self, value):
        self._street_address = value
    street_address = property(street_address, set_street_address)

    def city(self):
        return self._city
    def set_city(self, value):
        self._city = value
    city = property(city, set_city)

    def state(self):
        return self._state
    def set_state(self, value):
        pat = re.compile("[A-Z]{2}")
        if not pat.search(value):
            raise StateError('The state attribute must be a two-character, upper case, alphabetic string!')
        self._state = value
    def del_state(self):
        raise AttributeError
    state = property(state, set_state, del_state)

    def zip_code(self):
        return self._zip_code
    def set_zip_code(self, value):
        pat = re.compile("^[0-9]{5}$")
        if not pat.search(value):
            raise ZipCodeError("The zip_code attribute must a five-character string of integers! (leadings zeros are permitted)")
        self._zip_code = value
    def del_zip_code(self):
        raise AttributeError
    zip_code = property(zip_code, set_zip_code, del_zip_code)
