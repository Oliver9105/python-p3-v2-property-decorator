#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, name):
        """Name must be a string between 1 and 25 characters in length"""
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        """The breed property"""
        return self._breed

    @breed.setter
    def breed(self, breed):
        """Breed must be in the list of approved breeds"""
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be in list of approved breeds.")

# Testing the `Dog` class
if __name__ == "__main__":
    # Valid Dog instance
    fido = Dog("Fido", "Corgi")
    print(f"Dog's name: {fido.name}, Breed: {fido.breed}")
    
    # Invalid Dog instance
    try:
        invalid_dog = Dog(123, "Poodle")
    except ValueError as e:
        print(e)
    
    # Invalid breed
    try:
        snoopy = Dog("Snoopy", "Beagle")
        snoopy.breed = "Poodle"
    except ValueError as e:
        print(e)
