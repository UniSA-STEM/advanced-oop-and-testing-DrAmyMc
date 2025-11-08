'''
File: zoo.py
Description: A brief description of this Python module.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
'''

from enclosure import Enclosure
from staff import Staff

class Zoo:
    def __init__(self, name):
        self.name = name
        self.__enclosures = []
        self.__staff = []

    def get_name(self):
        return self.__name

    def get_enclosures(self):
        return self.__enclosures

    def get_staff(self):
        return self.__staff

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    name = property(get_name, set_name)
    enclosures = property(get_enclosures)
    staff = property(get_staff)

    def add_animal(self):
        pass

    def remove_animal(self):
        pass

    def add_enclosure(self, type, size):
        self.__enclosures.append(Enclosure(type,size))

    def remove_enclosure(self):
        pass

    def add_staff(self):
        pass

    def remove_staff(self):
        pass

    def assign_animal(self):
        pass

    def __str__(self):
        return f"{self.name} has {self.enclosures} enclosures and {self.staff} staff."