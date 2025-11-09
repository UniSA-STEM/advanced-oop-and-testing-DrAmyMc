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
    """
    Represents an animal in the abstract sense.
    The Animal class models general animal features, requirements, and methods.
    """

    def __init__(self, name, age, species):
        """
           Initialises a new Animal instance when utilised through a concrete subclass.

           Args:
               name (str): The name of the animal.
               age (int): The age of the animal.
               size (int): The species of the animal.

           Attributes:
               __name (str): The animal's name.
               __age (int): The animal's age.
               __species (str): The species of animal.
               __is_native (bool): Whether the animal species is native to Australia.
               __dietary_requirements (str): The diet of the animal species.
               __environment (str): The environment requirement of the animal species.
               __space (str): The amount of space required per animal of that animal species.
        """
        self.name = name                                    #Utilises the setter for validation of new instances
        self.age = age                                      #Utilises the setter for validation of new instances
        self.species = species                              #Utilises the setter for validation of new instances
        self.__is_native = self.__lookup_is_native()        #Utilises lookup function based on species
        self.__dietary_requirements = self.__lookup_diet()  #Utilises lookup function based on species
        self.__environment = self.__lookup_environment()    #Utilises lookup function based on species
        self.__space = self.__lookup_space()                #Utilises lookup function based on species

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
        """
        Updates the animal's name.

        Args:
            name (str): The new name for the animal, ensuring only a string may be passed.
        """
        if isinstance(name, str):
            self.__name = name

    def set_age(self, age):
        """
        Updates the animal's age, ensuring it remains within a valid range.

        Args:
            size (int): The new animal age (0-200) in years.
        """
        if isinstance(age, int) and 0 <= age <= 200:
            self.__age = age

    def set_species(self, species):
        """
        Sets the species type.

        Args:
            species (str): The species of the animal. Must be a valid species.
        """
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

    def __lookup_is_native(self)->bool:
        """Returns the species' native status."""
        return species_dict[self.species][3]

    def __lookup_diet(self)->str:
        """Returns the species' dietary requirements."""
        return species_dict[self.species][2]

    def __lookup_environment(self)->str:
        """Returns the species' environmental type."""
        return species_dict[self.species][0]

    def __lookup_space(self)->int:
        """Returns the species' space requirements."""
        return species_dict[self.species][1]

    # -------------------
    # Behavioural methods
    # -------------------

    def __str__(self):
        """
        Returns a formatted string containing the animal's details.

        Returns:
            str: The name, class, species, if native, age, and required environment, space, and diet.
        """
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

