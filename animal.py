"""
File: animal.py
Description: Abstract 'Animal' class for use in a Zoo.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod
from species import species_dict, loc_dict
from healthrecord import HealthRecord


class Animal(ABC):
    """
    Abstract base class representing a generic animal.
    This class defines shared attributes and behaviours common to all animals.
    Concrete subclasses (Mammal, Bird, Reptile, etc.) extend this class and may introduce additional
    attributes or override behaviour.

    Attributes:
        name (str): The animal's name.
        age (int): The animal's age.
        is_female (bool): The animal's sex (True if female, False if male)
        species (str): The species of animal.
        is_native (bool): Whether the animal species is native to Australia.
        dietary_requirements (str): The diet of the animal species.
        environment (str): The environment requirement of the animal species.
        space (str): The amount of space required per animal of that animal species.
        health_record (list): List of health records for the animal.
    """

    def __init__(self, name, age, is_female, species):
        """
        Initialises the shared attributes for an Animal.
        This constructor is intended to be called through a concrete subclass.

        Args:
            name (str): The name of the animal.
            age (int): The age of the animal.
            is_female (bool): The sex of the animal.
            species (str): The species of the animal.
        """
        self.name = name
        self.age = age
        self.is_female = is_female
        self.__is_native = None  # Will be overridden when species is set
        self.__dietary_requirements = None  # Will be overridden when species is set
        self.__environment = None  # Will be overridden when species is set
        self.__space = None  # Will be overridden when species is set
        self.species = species
        self.__health_record = []

    # --------------
    # Getter methods
    # --------------

    def get_name(self) -> str:
        """Returns the animal's name."""
        return self.__name

    def get_age(self) -> int:
        """Returns the animal's age."""
        return self.__age

    def get_is_female(self) -> bool:
        """Returns the animal's sex - True is female, False is male."""
        return self.__is_female

    def get_species(self) -> str:
        """Returns the animal's species."""
        return self.__species

    def get_is_native(self) -> bool:
        """Returns true/false for if the animal is native to Australia."""
        return self.__is_native

    def get_dietary_requirements(self) -> str:
        """Returns the animal's dietary requirements."""
        return self.__dietary_requirements

    def get_environment(self) -> str:
        """Returns the animal's required enclosure environment."""
        return self.__environment

    def get_space(self) -> int:
        """Returns the animal's space requirements in square metres."""
        return self.__space

    def get_health_record(self) -> list:
        """Returns the list of health records for the animal."""
        return self.__health_record

    # --------------
    # Setter methods
    # --------------

    def set_name(self, name):
        """
        Sets the animal's name.
        Args: name (str): The name for the animal, ensuring only a string of a minimum length may be passed.
        """
        MIN_LENGTH = 2
        if isinstance(name, str) and len(name) >= MIN_LENGTH:
            self.__name = name
        else:
            raise ValueError(f"Invalid animal name. Please enter text of at least {MIN_LENGTH} characters.")

    def set_age(self, age):
        """
        Sets the animal's age, ensuring it remains within a valid range.
        Args: size (int): The animal age (0-200) in years.
        """
        MIN_AGE = 0
        MAX_AGE = 200
        if isinstance(age, int) and MIN_AGE <= age <= MAX_AGE:
            self.__age = age
        else:
            raise ValueError(f"Invalid animal age. Please enter age in years, as an integer between "
                             f"{MIN_AGE} and {MAX_AGE}.")

    def set_is_female(self, is_female):
        """
        Sets the sex of the animal.
        Args: is_female (bool): True if female, False if male. Must be boolean.
        """
        if isinstance(is_female, bool):
            self.__is_female = is_female
        else:
            raise ValueError(f"Invalid sex. Please enter True if female or False if male.")

    def set_species(self, species):
        """
        Sets the species type and updates information related to species.
        Args: species (str): The species of the animal. Must be a valid species.
        """
        if str(species).title() in species_dict:
            self.__species = species.title()
            # Updates attributes determined by species type
            self.__is_native = self.__lookup_is_native()
            self.__dietary_requirements = self.__lookup_diet()
            self.__environment = self.__lookup_environment()
            self.__space = self.__lookup_space()
        else:
            raise ValueError(f"{species} is not a valid species. Please enter a valid species only.")

    # --------------------
    # Property definitions
    # --------------------

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    is_female = property(get_is_female, set_is_female)
    species = property(get_species, set_species)
    is_native = property(get_is_native)
    dietary_requirements = property(get_dietary_requirements)
    environment = property(get_environment)
    space = property(get_space)
    health_record = property(get_health_record)

    # --------------
    # Helper methods
    # --------------

    def __lookup_is_native(self) -> bool:
        """Returns the species' native status."""
        if self.species:
            return species_dict[self.species][loc_dict['native']]

    def __lookup_diet(self) -> str:
        """Returns the species' dietary requirements."""
        if self.species:
            return species_dict[self.species][loc_dict['diet']]

    def __lookup_environment(self) -> str:
        """Returns the species' environmental type."""
        if self.species:
            return species_dict[self.species][loc_dict['env']]

    def __lookup_space(self) -> int:
        """Returns the species' space requirements in square metres."""
        if self.species:
            return species_dict[self.species][loc_dict['space']]

    # -------------------
    # Behavioural methods
    # -------------------

    def add_health_record(self, record):
        """Adds a health record to the animals health record history."""
        if isinstance(record, HealthRecord):
            self.__health_record.append(record)
        else:
            raise ValueError("Not a health record object.")

    def __str__(self) -> str:
        """
        Returns a formatted string containing the animal's details.
        Returns: str: The name, class, species, if native, age, sex, and required environment, space, and diet.
        """
        native = "native" if self.is_native else "not native"
        sex = 'Female' if self.is_female else 'Male'
        return (f"---{self.name.upper()} THE {self.__class__.__name__.upper()}---\n"
                f"I am a {self.species}, which is {native} to Australia.\n"
                f"Age: {self.age} years old\n"
                f"Sex: {sex}\n"
                f"Required environment: {self.environment}\n"
                f"Required space: {self.space}m\u00b2\n"
                f"Required diet: {self.dietary_requirements}\n")

    # -----------------
    # Abstract methods
    # -----------------

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def move(self):
        pass
