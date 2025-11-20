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


class Enclosure:
    """
    Represents an enclosure in a zoo, of a particular type and size.

    Attributes:
        name (str): The enclosure's name.
        type (str): The envrionmental type of the enclosure.
        size (int): The size of the enclosure in square metres.
        cleanliness_level (int): The cleanliness of the enclosure from 0 (filthy) to 5 (pristine).
        animal_type (str | None): The type of animal housed in the enclosure, None if empty.
        animals_housed (list[Animal]): A list of animal objects in the enclosure, initially empty.
        assigned_keeper (obj): The zookeeper assigned to the enclosure.
        assigned_vet (obj): The vet assigned to the enclosure.
    """

    # List of the valid enclosure types
    TYPE_LIST = ["Aquatic", "Savannah", "Terrarium", "Bushland", "Forest", "Jungle", "Aviary"]

    def __init__(self, name, type, size):
        """
        Initialises a new Enclosure instance.

        Args:
            name (str): The name of the enclosure.
            type (str): The environmental type of the enclosure.
            size (int): The size of the enclosure in square metres.
        """
        self.name = name  # Utilises the setter for validation of new instances
        self.type = type  # Utilises the setter for validation of new instances
        self.size = size  # Utilises the setter for validation of new instances
        self.__cleanliness_level = 5
        self.__animal_type = None
        self.__animals_housed = []
        self.__assigned_keeper = None
        self.__assigned_vet = None

    # --------------
    # Getter methods
    # --------------

    def get_name(self) -> str:
        """Returns the enclosure's name."""
        return self.__name

    def get_type(self) -> str:
        """Returns the enclosure's environmental type."""
        return self.__type

    def get_size(self) -> int:
        """Returns the enclosure's size in square metres."""
        return self.__size

    def get_cleanliness_level(self) -> int:
        """Returns the enclosure's cleanliness level."""
        return self.__cleanliness_level

    def get_animal_type(self) -> str:
        """Returns the enclosure's animal type or None if empty."""
        return self.__animal_type

    def get_animals_housed(self) -> list:
        """Returns the list of animals housed in the enclosure."""
        return self.__animals_housed

    def get_assigned_keeper(self):
        """Returns the zookeeper assigned to the enclosure."""
        return self.__assigned_keeper

    def get_assigned_vet(self):
        """Returns the veterninarian assigned to the enclosure."""
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
            raise ValueError(f"Invalid enclosure name. Please enter text of at least {MIN_LENGTH} characters.")

    def set_type(self, type):
        """
        Sets the environmental type of the enclosure.
        Args: type (str): The environmental type of the enclosure. Must be a valid type.
        """
        if type.title() in Enclosure.TYPE_LIST:
            self.__type = type.title()
        else:
            raise ValueError(f"Invalid enclosure type. Please enter one of the following types: "
                  f"{Enclosure.TYPE_LIST}")

    def set_size(self, size):
        """
        Sets the enclosure size, ensuring it remains within a valid range.
        Args: size (int): The new enclosure size (0-5000) in square metres.
        """
        MIN_SIZE = 1
        MAX_SIZE = 5000
        if isinstance(size, int) and MIN_SIZE <= size <= MAX_SIZE:
            self.__size = size
        else:
            raise ValueError(f"Invalid size. Please enter an integer between {MIN_SIZE} and {MAX_SIZE}.")

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
            raise ValueError(f"Invalid cleanliness level. Please enter an integer between {MIN_LEVEL} and {MAX_LEVEL}.")

    def set_animal_type(self, species):
        """
        Sets the species to be housed in the enclosure.
        Args: species (str): The species to be housed in the enclosure. Must be a valid species.
        """
        if str(species).title() in species_dict:
            self.__animal_type = species.title()
        else:
            raise ValueError(f"{species} is not a valid species. Please enter a valid species only.")

    def set_assigned_keeper(self, keeper):
        """Sets the assigned keeper to zookeeper name."""
        self.__assigned_keeper = keeper

    def set_assigned_vet(self, vet):
        """Sets the assigned vet to veterinarian name."""
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
    assigned_keeper = property(get_assigned_keeper, set_assigned_keeper)
    assigned_vet = property(get_assigned_vet, set_assigned_vet)

    # --------------
    # Helper methods
    # --------------

    def calculate_max_animals(self) -> int | None:
        """
        Calculates maximum number of animals that can be held based on enclosure size
        and space requirements for the species housed.
        Returns: max_animals
        """
        if self.animal_type is not None:
            species_space = species_dict[self.animal_type][loc_dict['space']]
            max_animals = self.size // species_space
            return max_animals

    def be_cleaned(self):
        """Returns the enclosure to a cleaned state."""
        self.cleanliness_level = 5

    def lookup_feed(self):
        if self.animal_type is not None:
            species_feed = species_dict[self.animal_type][loc_dict['diet']]
            return species_feed

    # -------------------
    # Behavioural methods
    # -------------------

    def report_status(self)->str:
        """Returns a cleanliness status message based on current cleanliness level."""
        if self.cleanliness_level == 0:
            return "This enclosure is filthy. Immediate action is required."
        elif self.cleanliness_level == 1:
            return "This enclosure is very dirty. It should be cleaned urgently."
        elif self.cleanliness_level == 2:
            return "This enclosure is now dirty. It should be cleaned now."
        elif self.cleanliness_level == 3:
            return "This enclosure is becoming dirty. It should be cleaned soon."
        elif self.cleanliness_level == 4:
            return "This enclosure is quite clean. It does not need cleaning yet."
        else:
            return "This enclosure is pristine. It has just been cleaned."

    def become_poopy(self)->str:
        if self.animal_type is None:
            return f"{self.name} has no animals in the enclosure to poop in it."
        else:
            if self.cleanliness_level > 0:
                self.cleanliness_level -= 1
            return f"{self.name} is becoming dirtier as the {self.animal_type}s poop. " + self.report_status()

    def add_animal(self, animal):
        """
        Adds an animal to the enclosure.
        Args: animal (Animal): Adds an animal to the list of animals housed in the enclosure. Must be Animal class.
        """
        # Ensures only animal objects can be added to enclosure
        if not isinstance(animal, Animal):
            raise ValueError(f"This is not an animal. Cannot add to enclosure.")
        # Ensures environmental type of enclosure is suitable for species being added
        elif animal.environment != self.type:
            raise ValueError(f"Cannot add {animal.species} to this {self.type} enclosure - must be in {animal.environment} enclosure.")
        # Ensures enclosure is restricted to a single type of animal as per assignment specification
        elif self.animal_type is not None and self.animal_type != animal.species:
            raise ValueError(f"Cannot add {animal.species} to this {self.animal_type} enclosure - must be same species.")
        # Ensures enclosure has enough space before successfully adding animal when enclosure emptu.
        elif self.animal_type is None and self.size < animal.space:
            raise ValueError(f"Cannot add {animal.species} - you need a bigger enclosure of at least {animal.space}m\u00b2.")
        # Adds animal to empty enclosure of appropriate size and type.
        elif self.animal_type is None and self.size >= animal.space:
            self.__animals_housed.append(animal)
            # Sets animal type of enclosure when first species successfully added
            self.animal_type = animal.species
            return f"You have successfully added a {animal.species}. This is now a {self.animal_type} enclosure."
        # Ensures enclosure has enough space before adding animal when animals already present.
        elif len(self.animals_housed) >= self.calculate_max_animals():
            raise ValueError(f"Cannot add {animal.species} - the enclosure is already full of {animal.species}s.")
        # Adds animal to enclosure of appropriate size and type with same species
        else:
            self.__animals_housed.append(animal)
            return(f"You have successfully added another {animal.species} to this enclosure.")

    def list_animals(self)-> str:
        """Returns a list of animals housed in enclosure."""
        if self.animals_housed == []:
            animals_housed_str = f"{self.name} is currently empty.\n"
        else:
            animals_housed_str = f"---Animals Housed in {self.name}---\n"
            for animal in self.animals_housed:
                animals_housed_str += (f"{animal.name} the {animal.species}, aged {animal.age} years\n")
        return animals_housed_str

    def check_capacity(self)->str:
        """Returns a capacity message based on current capacity of enclosure."""
        if self.animal_type is None:
            return f"This enclosure is currently empty. It has {self.size}m\u00b2 of space available."
        else:
            # Calculates current, maximum, and available animal numbers
            current_animals = len(self.animals_housed)
            max_animals = self.calculate_max_animals()
            space_available = max_animals - current_animals
            # Message re: current animal numbers
            current = f"This enclosure currently houses {current_animals} {self.animal_type}s. "
            # Custom capacity message based on whether space is available or not
            if space_available > 0:
                available = f"It has space available for {space_available} more {self.animal_type}s."
            else:
                available = "It is at maximum capacity and has no more space available."
            return current + available

    def __str__(self)->str:
        """
        Returns a formatted string containing the enclosure's details.
        Returns: str: The enclosure name, type, size, cleanliness level, and animal species housed.
        """
        if self.animal_type is None:
            animal_type = f"This enclosure is currently empty.\n"
        else:
            animal_type = f"Houses: {len(self.animals_housed)} {self.animal_type}s\n"
        return [f"---{self.name.upper()}---\n"
                f"{self.type} Enclosure\n"
                f"Size: {self.size}m\u00b2\n"
                f"Cleanliness level: {self.cleanliness_level}\n"
                f"Assigned zookeeper: {self.assigned_keeper.first_name} {self.assigned_keeper.last_name}\n"
                f"Assigned veterinarian: {self.assigned_vet.first_name} {self.assigned_vet.last_name}\n"
                f"{animal_type}\n"]