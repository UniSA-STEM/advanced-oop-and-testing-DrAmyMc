"""
File: zoo.py
Description: Zoo class, representing a zoo and its operations with enclosures, animals, and staff.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from enclosure import Enclosure
from staff import Staff


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__enclosures = []
        self.__staff = []

    # --------------
    # Getter methods
    # --------------

    def get_name(self)->str:
        """Returns the zoo's name."""
        return self.__name

    def get_enclosures(self)->list:
        """Returns the list of enclosure objects at the zoo."""
        return self.__enclosures

    def get_staff(self)->list:
        """Returns the list of staff objects at the zoo."""
        return self.__staff

    # --------------
    # Setter methods
    # --------------

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    # --------------------
    # Property definitions
    # --------------------

    name = property(get_name, set_name)
    enclosures = property(get_enclosures)
    staff = property(get_staff)

    # -------------------
    # Behavioural methods
    # -------------------

    def add_animal(self):
        pass

    def remove_animal(self):
        pass

    def add_enclosure(self, name, type, size):
        self.__enclosures.append(Enclosure(name, type,size))

    def remove_enclosure(self):
        pass

    def add_staff(self):
        pass

# TODO: Fix name parameter for removal
    def remove_staff(self, staff_name):
        if staff_name in self.staff.name:
            self.staff.remove(staff_name)

# TODO: Fix animal / enclosure parameters
    def assign_animal(self, animal, enclosure):
        if enclosure.animal_type is None:
            enclosure.animal_type(animal.species)
            enclosure.add_animal(animal)
        elif enclosure.animal_type == animal.species:
            enclosure.add_animal(animal)
        else:
            print(f"Cannot add to this enclosure - must be of species {enclosure.animal_type}.")

    def __str__(self):
        return f"{self.name} has {self.enclosures} enclosures and {self.staff} staff.\n"