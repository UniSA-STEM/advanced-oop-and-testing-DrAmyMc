"""
File: animal.py
Description: Abstract 'Animal' class and its concrete subclasses, for use in a Zoo.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod
from species import species_dict


class Animal(ABC):
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self.__is_native = self.__lookup_is_native()
        self.__dietary_requirements = self.__lookup_diet()
        self.__environment = self.__lookup_environment()
        self.__space = self.__lookup_space()

    # --------------
    # Getter methods
    # --------------

    def get_name(self)->str:
        """Returns the animal's name."""
        return self.__name

    def get_age(self)->int:
        """Returns the animal's age."""
        return self.__age

    def get_species(self)->str:
        """Returns the animal's species."""
        return self.__species

    def get_is_native(self)->bool:
        """Returns true/false for if the animal is native to Australia."""
        return self.__is_native

    def get_dietary_requirements(self)->str:
        """Returns the animal's dietary requirements."""
        return self.__dietary_requirements

    def get_environment(self)->str:
        """Returns the animal's required enclosure environment."""
        return self.__environment

    def get_space(self)->int:
        """Returns the animal's space requirements in square metres."""
        return self.__space

    # --------------
    # Setter methods
    # --------------

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 200:
            self.__age = age

    def set_species(self, species):
        if species in species_dict:
            self.__species = species

    # --------------------
    # Property definitions
    # --------------------

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    species = property(get_species, set_species)
    is_native = property(get_is_native)
    dietary_requirements = property(get_dietary_requirements)
    environment = property(get_environment)
    space = property(get_space)

    # -------------------
    # Helper methods
    # -------------------

    def __lookup_is_native(self):
        return species_dict[self.species][3]

    def __lookup_diet(self):
        return species_dict[self.species][2]

    def __lookup_environment(self):
        return species_dict[self.species][0]

    def __lookup_space(self):
        return species_dict[self.species][1]

    # -------------------
    # Behavioural methods
    # -------------------

    def __str__(self):
        details = [f"---{self.name.upper()} THE {self.__class__.__name__.upper()}---"]
        if self.is_native:
            details.append(f"I am a {self.species}, which is native to Australia.")
        else:
            details.append(f"I am a {self.species}, which is not native to Australia.")
        details.append(f"Age: {self.age} years old\n"
                       f"Required environment: {self.environment}\n"
                       f"Required space: {self.space}m\u00b2\n"
                       f"Required diet: {self.dietary_requirements}\n")
        return '\n'.join(details)

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


class Carnivore(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    # -------------------
    # Behavioural methods
    # -------------------

    def make_sound(self):
        return "Roar!"

    def eat(self):
        return f"{self.name} is now eating {self.dietary_requirements}."

    def sleep(self):
        return f"{self.name} is now sleeping."

    def move(self):
        return f"{self.name} is now moving."

    def __str__(self):
        return super().__str__()

