"""
File: enclosure.py
Description: Enclosure class, representing an enclosure in a zoo to hold animals.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal
from species import species_dict, loc_dict
from staff import Zookeeper
from staff import Veterinarian


class Enclosure:
    """
    Represents an enclosure in a zoo, of a particular type and size.
    """

    # List of the valid enclosure types
    TYPE_LIST = ["Aquatic", "Savannah", "Terrarium", "Bushland", "Forrest", "Jungle", "Aviary"]

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
        self.__assigned_zookeeper = None
        self.__assigned_vet = None

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

    def get_assigned_zookeeper(self):
        """Returns the name of the zookeeper assigned to the enclosure."""
        return self.__assigned_zookeeper

    def get_assigned_vet(self):
        """Returns the name of the vet assigned to the enclosure."""
        return self.__assigned_vet

    # --------------
    # Setter methods
    # --------------

    def set_name(self, name):
        """
        Sets the enclosure's name.
        Args: name (str): The name for the enclosure, ensuring only a string of a minimum length may be passed.
        """
        MIN_LENGTH = 3
        if isinstance(name, str) and len(name) >= MIN_LENGTH:
            self.__name = name
        else:
            print(f"Invalid enclosure name. Please enter text of at least {MIN_LENGTH} characters.")

    def set_type(self, type):
        """
        Sets the environmental type of the enclosure.
        Args: type (str): The environmental type of the enclosure. Must be a valid type.
        """
        if type in Enclosure.TYPE_LIST:
            self.__type = type
        else:
            print(f"Invalid enclosure type. Please enter one of the following types: "
                  f"{Enclosure.TYPE_LIST}")

    def set_size(self, size):
        """
        Updates the enclosure size, ensuring it remains within a valid range.
        Args: size (int): The new enclosure size (0-5000) in square metres.
        """
        MIN_SIZE = 1
        MAX_SIZE = 5000
        if isinstance(size, int) and MIN_SIZE <= size <= MAX_SIZE:
            self.__size = size
        else:
            print(f"Invalid size. Please enter an integer between {MIN_SIZE} and {MAX_SIZE}.")

    def set_cleanliness_level(self, level):
        """
        Updates the cleanliness level, ensuring it remains within a valid range.
        Args: cleanliness_level (int): The new cleanliness level (0-5).
        """
        MIN_LEVEL = 0
        MAX_LEVEL = 5
        if isinstance(level, int) and MIN_LEVEL <= level <= MAX_LEVEL:
            self.__cleanliness_level = level
        else:
            print(f"Invalid cleanliness level. Please enter an integer between {MIN_LEVEL} and {MAX_LEVEL}.")

    def set_animal_type(self, species):
        """
        Sets the species to be housed in the enclosure.
        Args: species (str): The species to be housed in the enclosure. Must be a valid species.
        """
        if species.title() in species_dict:
            self.__animal_type = species.title()
        else:
            print(f"{species.title()} is not a valid species. Please enter a valid species only.")

    def set_assigned_zookeeper(self, zookeeper):
        if isinstance(zookeeper, Zookeeper):
            self.__assigned_zookeeper = zookeeper

    def set_assigned_vet(self, vet):
        if isinstance(vet, Veterinarian):
            self.__assigned_vet = vet

    # --------------------
    # Property definitions
    # --------------------

    name = property(get_name, set_name)
    type = property(get_type, set_type)
    size = property(get_size, set_size)
    cleanliness_level = property(get_cleanliness_level, set_cleanliness_level)
    animal_type = property(get_animal_type, set_animal_type)
    animals_housed = property(get_animals_housed)
    assigned_zookeeper = property(get_assigned_zookeeper, set_assigned_zookeeper)
    assigned_vet = property(get_assigned_vet, set_assigned_vet)

    # --------------
    # Helper methods
    # --------------

    def calculate_max_animals(self)->int:
        """
        Calculates maximum number of animals that can be held based on enclosure size
        and space requirements for the species housed.

        Returns: max_animals
        """
        if self.animal_type is not None:
            species_space = species_dict[self.animal_type][loc_dict['space']]
            max_animals = self.size // species_space
            return max_animals

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
        # Ensures only animal objects can be added to enclosure
        if not isinstance(animal, Animal):
            print(f"This is not an animal. Cannot add to enclosure.")
        # Ensures environmental type of enclosure is suitable for species being added
        elif animal.environment != self.type:
            print(f"Cannot add {animal.species} to this {self.type} enclosure - must be in {animal.environment} enclosure.")
        # Ensures enclosure is restricted to a single type of animal as per assignment specification
        elif self.animal_type is not None and self.animal_type != animal.species:
            print(f"Cannot add {animal.species} to this {self.animal_type} enclosure - must be same species.")
        # Ensures enclosure has enough space before successfully adding animal
        elif self.animal_type is None and self.size < animal.space:
            print(f"Cannot add {animal.species} - you need a bigger enclosure of at least {animal.size}m\u00b2.")
        elif self.animal_type is None and self.size >= animal.space:
            self.__animals_housed.append(animal)
            # Sets animal type of enclosure when first species successfully added
            self.animal_type = animal.species
            print(f"You have successfully added a {animal.species}. This is now a {self.animal_type} enclosure.")
        elif len(self.animals_housed) >= self.calculate_max_animals():
            print(f"Cannot add {animal.species} - the enclosure is already full of {animal.species}s.")
        else:
            self.__animals_housed.append(animal)
            print(f"You have successfully added another {animal.species} to this enclosure.")

    def list_animals(self):
        """Prints a list of animals housed in enclosure."""
        if self.animals_housed == []:
            animals_housed_str = f"{self.name} is currently empty.\n"
        else:
            animals_housed_str = f"---Animals Housed in {self.name}---\n"
            for animal in self.animals_housed:
                animals_housed_str += (f"{animal.name} the {animal.species}, aged {animal.age} years\n")
        print(animals_housed_str)

    def report_status(self):
        """Prints a cleanliness status message based on current cleanliness level."""
        if self.cleanliness_level == 0:
            print("This enclosure is filthy. Immediate action is required.")
        elif self.cleanliness_level == 1:
            print("This enclosure is very dirty. It should be cleaned urgently.")
        elif self.cleanliness_level == 2:
            print("This enclosure is now dirty. It should be cleaned now.")
        elif self.cleanliness_level == 3:
            print("This enclosure is becoming dirty. It should be cleaned soon.")
        elif self.cleanliness_level == 4:
            print("This enclosure is quite clean. It does not need cleaning yet.")
        else:
            print("This enclosure is pristine. It has just been cleaned.")

    def check_capacity(self):
        """Prints a capacity message based on current capacity of enclosure."""
        if self.animal_type is None:
            print(f"This enclosure is currently empty. It has {self.size}m\u00b2 of space available.")
        else:
            # Calculates current, maximum, and available animal numbers
            current_animals = len(self.animals_housed)
            max_animals = self.calculate_max_animals()
            space_available = max_animals - current_animals
            # Displays current animal numbers
            print(f"This enclosure currently houses {current_animals} {self.animal_type}s.")
            # Displays custom capacity message based on whether space is available or not
            if space_available > 0:
                print(f"It has space available for {space_available} more {self.animal_type}s.")
            else:
                print("It is at maximum capacity and has no more space available.")

    def __str__(self):
        """
        Returns a formatted string containing the enclosure's details.
        Returns: str: The enclosure name, type, size, cleanliness level, and animal species housed.
        """
        try:
            if self.assigned_zookeeper is None:
                zookeeper = 'None assigned'
            else:
                zookeeper = f"{self.assigned_zookeeper.first_name} {self.assigned_zookeeper.last_name}"
            if self.assigned_vet is None:
                vet = 'None assigned'
            else:
                vet = f"{self.assigned_vet.first_name} {self.assigned_vet.last_name}"
            if self.animal_type is None:
                animal_type = f"This enclosure is currently empty.\n"
            else:
                animal_type = f"Houses: {len(self.animals_housed)} {self.animal_type}s\n"
            return [f"---{self.name.upper()}---\n"
                    f"{self.type} Enclosure\n"
                    f"Size: {self.size}m\u00b2\n"
                    f"Cleanliness level: {self.cleanliness_level}\n"
                    f"Assigned zookeeper: {zookeeper}\n"
                    f"Assigned veterinarian: {vet}\n"
                    f"{animal_type}\n"]
        except:
            return "Invalid object.\n"