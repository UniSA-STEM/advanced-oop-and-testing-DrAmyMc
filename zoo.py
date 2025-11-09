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
    """
    Represents a zoo, with enclosures, animals and staff.
    """

    def __init__(self, name):
        """
           Initialises a new Zoo instance.

           Args:
               name (str): The name of the zoo.

           Attributes:
               __name (str): The zoo's name.
               __enclosures (list[Enclosure]): A list of Enclosure objects at the zoo, initially empty.
               __staff (list[Staff]): A list of Staff objects at the zoo, initially empty.
        """
        self.name = name            #Utilises the setter for validation of new instances
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
        """
        Updates the zoo's name.

        Args:
            name (str): The new name for the zoo, ensuring only a string of a minimum length may be passed.
        """
        MIN_LENGTH = 3
        if isinstance(name, str) and len(name) >= MIN_LENGTH:
            self.__name = name
        else:
            print(f"Invalid zoo name. Please enter text of at least {MIN_LENGTH} characters.")

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

    #TODO: Update with different format to list enclosures and staff properly
    def __str__(self)->str:
        """
        Returns a formatted string containing the zoo's details.

        Returns:
            str: The name, enclosure list, and staff list.
        """
        try:
            return f"{self.name} has {self.enclosures} enclosures and {self.staff} staff.\n"
        except:
            return "Invalid object.\n"
