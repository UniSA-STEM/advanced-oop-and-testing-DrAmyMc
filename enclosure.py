'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Enclosure:
    TYPE_LIST = ["Aquatic", "Savannah", "Terrarium", "Bushland"]

    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size
        self.__cleanliness_level = 5
        self.__animal_type = None
        self.__animals_housed = []

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_size(self):
        return self.__size

    def get_cleanliness_level(self):
        return self.__cleanliness_level

    def get_animal_type(self):
        return self.__animal_type

    def get_animals_housed(self):
        return self.__animals_housed

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def set_type(self, type):
        if type in Enclosure.TYPE_LIST:
            self.__type = type

    def set_size(self, size):
        if isinstance(size, int) and 0 < size < 5000:
            self.__size = size

    def set_cleanliness_level(self, level):
        if isinstance(level, int) and 0 <= level <= 5:
            self.__cleanliness_level = level

    def set_animal_type(self, species):
        self.__animal_type = species

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.__animals_housed.append(animal)

    name = property(get_name, set_name)
    type = property(get_type, set_type)
    size = property(get_size, set_size)
    cleanliness_level = property(get_cleanliness_level, set_cleanliness_level)
    animal_type = property(get_animal_type, set_animal_type)
    animals_housed = property(get_animals_housed)

    def __str__(self):
        details = [f"---{self.type.upper()} ENCLOSURE---\n"
                f"Size: {self.size}m\u00b2\n"
                f"Cleanliness level: {self.cleanliness_level}"]
        if self.cleanliness_level == 0:
            details.append(f"This enclosure urgently needs cleaning!")
        if self.animal_type is None:
            details.append(f"This enclosure is currently empty.\n")
        else:
            details.append(f"This enclosures houses the {self.animal_type} species.")
        return '\n'.join(details)