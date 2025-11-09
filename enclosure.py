"""
File: enclosure.py
Description: Enclosure class, representing an enclosure in a zoo to hold animals.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal
from species import species_dict


class Enclosure:
    """
    Represents an enclosure in a zoo, of a particular type and size.
    """

    # List of the valid enclosure types
    TYPE_LIST = ["Aquatic", "Savannah", "Terrarium", "Bushland"]

    def __init__(self, name, type, size):
        """
           Initialises a new Enclosure instance.

           Args:
               name (str): The name of the enclosure.
               type (str): The environmental type of the enclosure.
               size (int): The size of the enclosure in square metres.

           Attributes:
               __name (str): The enclosure's name.
               __type (str): The envrionmental type of the enclosure.
               __size (int): The size of the enclosure in square metres.
               __cleanliness_level (int): The cleanliness of the enclosure from 0 (filthy) to 5 (pristine).
               __animal_type (str | None): The type of animal housed in the enclosure, None if empty.
               __animals_housed = (list[Animal]): A list of animal objects in the enclosure, initially empty.
        """
        self.name = name                #Utilises the setter for validation of new instances
        self.type = type                #Utilises the setter for validation of new instances
        self.size = size                #Utilises the setter for validation of new instances
        self.__cleanliness_level = 5
        self.__animal_type = None
        self.__animals_housed = []

    # --------------
    # Getter methods
    # --------------

    def get_name(self)->str:
        """Returns the enclosure's name."""
        return self.__name

    def get_type(self)->str:
        """Returns the enclosure's environmental type."""
        return self.__type

    def get_size(self)->int:
        """Returns the enclosure's size in square metres."""
        return self.__size

    def get_cleanliness_level(self)->int:
        """Returns the enclosure's cleanliness level."""
        return self.__cleanliness_level

    def get_animal_type(self)->str:
        """Returns the enclosure's animal type or None if empty."""
        return self.__animal_type

    def get_animals_housed(self)->list:
        """Returns the list of animals housed in the enclosure."""
        return self.__animals_housed

    # --------------
    # Setter methods
    # --------------

    def set_name(self, name):
        """
        Updates the enclosure's name.

        Args:
            name (str): The new name for the enclosure, ensuring only a string may be passed.
        """
        if isinstance(name, str):
            self.__name = name

    def set_type(self, type):
        """
        Sets the environmental type of the enclosure.

        Args:
            type (str): The environtmental type of the enclosure. Must be a valid type.
        """
        if type in Enclosure.TYPE_LIST:
            self.__type = type

    def set_size(self, size):
        """
        Updates the enclosure size, ensuring it remains within a valid range.

        Args:
            size (int): The new enclosure size (0-5000) in square metres.
        """
        if isinstance(size, int) and 0 < size <= 5000:
            self.__size = size

    def set_cleanliness_level(self, level):
        """
        Updates the cleanliness level, ensuring it remains within a valid range.

        Args:
            cleanliness_level (int): The new cleanliness level (0-5).
        """
        if isinstance(level, int) and 0 <= level <= 5:
            self.__cleanliness_level = level

    def set_animal_type(self, species):
        """
        Sets the species to be housed in the enclosure.

        Args:
            species (str): The species to be housed in the enclosure. Must be a valid species.
        """
        if species in species_dict:
            self.__animal_type = species

    # --------------------
    # Property definitions
    # --------------------

    name = property(get_name, set_name)
    type = property(get_type, set_type)
    size = property(get_size, set_size)
    cleanliness_level = property(get_cleanliness_level, set_cleanliness_level)
    animal_type = property(get_animal_type, set_animal_type)
    animals_housed = property(get_animals_housed)

    # -------------------
    # Behavioural methods
    # -------------------

    def add_animal(self, animal):
        """
        Adds an animal to the enclosure.

        Args:
            animal (Animal): Adds an animal to the list of animals housed in the enclosure.
                             Must be Animal class.
        """
        if isinstance(animal, Animal):
            self.__animals_housed.append(animal)

    def __str__(self):
        """
        Returns a formatted string containing the enclosure's details.

        Returns:
            str: The enclosure name, type, size, cleanliness level, and animal species housed.
        """
        details = [f"---{self.name.upper()}---\n"
                   f"{self.type} Enclosure---\n"
                   f"Size: {self.size}m\u00b2\n"
                   f"Cleanliness level: {self.cleanliness_level}"]
        if self.cleanliness_level == 0:
            details.append(f"This enclosure urgently needs cleaning!")
        if self.animal_type is None:
            details.append(f"This enclosure is currently empty.\n")
        else:
            details.append(f"This enclosures houses the {self.animal_type} species.")
        return '\n'.join(details)