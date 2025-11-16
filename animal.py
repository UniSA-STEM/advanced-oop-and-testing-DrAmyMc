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
from species import loc_dict
from healthrecord import HealthRecord


class Animal(ABC):
    """
    Represents an animal in the abstract sense.
    The Animal class models general animal features, requirements, and methods.
    """

    def __init__(self, name, age, is_female, species):
        """
           Initialises a new Animal instance when utilised through a concrete subclass.

           Args:
               name (str): The name of the animal.
               age (int): The age of the animal.
               is_female (bool): The sex of the animal.
               species (str): The species of the animal.

           Attributes:
               __name (str): The animal's name.
               __age (int): The animal's age.
               __is_female (bool): The animal's sex (True if female, False if male)
               __species (str): The species of animal.
               __is_native (bool): Whether the animal species is native to Australia.
               __dietary_requirements (str): The diet of the animal species.
               __environment (str): The environment requirement of the animal species.
               __space (str): The amount of space required per animal of that animal species.
        """
        self.name = name                        # Utilises the setter for validation of new instances
        self.age = age                          # Utilises the setter for validation of new instances
        self.is_female = is_female              # Utilises the setter for validation of new instances
        self.__is_native = None                 # Will be overridden when species is set
        self.__dietary_requirements = None      # Will be overridden when species is set
        self.__environment = None               # Will be overridden when species is set
        self.__space = None                     # Will be overridden when species is set
        self.species = species                  # Utilises the setter for validation of new instances
        self.__health_record = []

    # --------------
    # Getter methods
    # --------------

    def get_name(self)->str:
        """Returns the animal's name."""
        return self.__name

    def get_age(self)->int:
        """Returns the animal's age."""
        return self.__age

    def get_is_female(self)->bool:
        """Returns the animal's sex - True is female, False is male."""
        return self.__is_female

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

    def get_health_record(self)->list:
        """Returns the list of health records for the animal."""
        return self.__health_record

    # --------------
    # Setter methods
    # --------------

    def set_name(self, name):
        """
        Updates the animal's name.

        Args:
            name (str): The new name for the animal, ensuring only a string of a minimum length may be passed.
        """
        MIN_LENGTH = 2
        if isinstance(name, str) and len(name) >= MIN_LENGTH:
            self.__name = name
        else:
            print(f"Invalid animal name. Please enter text of at least {MIN_LENGTH} characters.")

    def set_age(self, age):
        """
        Updates the animal's age, ensuring it remains within a valid range.

        Args:
            size (int): The new animal age (0-200) in years.
        """
        MIN_AGE = 0
        MAX_AGE = 200
        if isinstance(age, int) and MIN_AGE <= age <= MAX_AGE:
            self.__age = age
        else:
            print(f"Invalid animal age. Please enter age in years, as an integer between "
                  f"{MIN_AGE} and {MAX_AGE}.")

    def set_is_female(self, is_female):
        """
        Sets the sex of the animal.

        Args:
            is_female (bool): True if female, False if male. Must be boolean.
        """
        if isinstance(is_female, bool):
            self.__is_female = is_female
        else:
            print(f"Invalid sex. Please enter True if female or False if male.")

    def set_species(self, species):
        """
        Sets the species type and updates information related to species.

        Args:
            species (str): The species of the animal. Must be a valid species.
        """
        if species.title() in species_dict:
            self.__species = species.title()
            # Updates attributes determined by species type
            self.__is_native = self.__lookup_is_native()
            self.__dietary_requirements = self.__lookup_diet()
            self.__environment = self.__lookup_environment()
            self.__space = self.__lookup_space()
        else:
            print(f"{species.title()} is not a valid species. Please enter a valid species only.")

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

    def __lookup_is_native(self)->bool:
        """Returns the species' native status."""
        if self.species:
            return species_dict[self.species][loc_dict['native']]

    def __lookup_diet(self)->str:
        """Returns the species' dietary requirements."""
        if self.species:
            return species_dict[self.species][loc_dict['diet']]

    def __lookup_environment(self)->str:
        """Returns the species' environmental type."""
        if self.species:
            return species_dict[self.species][loc_dict['env']]

    def __lookup_space(self)->int:
        """Returns the species' space requirements."""
        if self.species:
            return species_dict[self.species][loc_dict['space']]

    # -------------------
    # Behavioural methods
    # -------------------

    def add_health_record(self, issue_type, severity_level, date_reported, description, treatment_plan):
        """
        Initialises a new Health Record instance for the animal.

        Args:
            issue_type (str): The category of issue being reported.
            severity_level (int): The severity level from 0-3.
            date_reported (str): The date of the initial report.
            description (str): A description of the health issue
            treatment_plan (str): The initial treatment plan/notes.
        """
        new_record = HealthRecord(issue_type, severity_level, date_reported, description, treatment_plan)
        self.health_record.append(new_record)
        print(f"New health record created:\n"
              f"{new_record}")

    def __str__(self):
        """
        Returns a formatted string containing the animal's details.

        Returns:
            str: The name, class, species, if native, age, sex, and required environment, space, and diet.
        """
        try:
            sex = 'Female' if self.is_female else 'Male'
            details = [f"---{self.name.upper()} THE {self.__class__.__name__.upper()}---"]
            if self.is_native:
                details.append(f"I am a {self.species}, which is native to Australia.")
            else:
                details.append(f"I am a {self.species}, which is not native to Australia.")
            details.append(f"Age: {self.age} years old\n"
                           f"Sex: {sex}\n"
                           f"Required environment: {self.environment}\n"
                           f"Required space: {self.space}m\u00b2\n"
                           f"Required diet: {self.dietary_requirements}")
            return '\n'.join(details)
        except:
            return "Invalid object.\n"

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


class Mammal(Animal):
    def __init__(self, name, age, species, is_female):
        super().__init__(name, age, species, is_female)
        self.__is_pregnant = False

    # --------------
    # Getter methods
    # --------------

    def get_is_pregnant(self)->bool:
        """Returns the animal's pregnancy status - True or False."""
        return self.__is_pregnant

    # --------------
    # Setter methods
    # --------------

    def set_is_pregnant(self, is_pregnant):
        """
        Sets the pregnancy status of the mammal.

        Args:
            is_pregnant (bool): True if pregnant, False if not pregnant. Must be boolean.
        """
        if isinstance(is_pregnant, bool) and self.is_female:
            self.__is_pregnant = is_pregnant

    # --------------------
    # Property definitions
    # --------------------

    is_pregnant = property(get_is_pregnant, set_is_pregnant)

    # -------------------
    # Behavioural methods
    # -------------------

    def make_sound(self):
        return "Roar!"

    def eat(self):
        return f"{self.name} is eating their {self.dietary_requirements}."

    def sleep(self):
        return f"{self.name} is sleeping."

    def move(self):
        return f"{self.name} is walking around their enclosure."

    def __str__(self):
        return super().__str__() + f"Mammal\n"


class Bird(Animal):
    def __init__(self, name, age, species, is_flightless):
        super().__init__(name, age, species)
        self.is_flightless = is_flightless

    # --------------
    # Getter methods
    # --------------

    def get_is_flightless(self)->bool:
        """Returns whether the bird is flightless."""
        return self.__is_flightless

    # --------------
    # Setter methods
    # --------------

    def set_is_flightless(self, is_flightless):
        """
       Sets whether the bird is flightless.

       Args:
           is_flightless (bool): True if flightless, False if able to fly. Must be boolean.
       """
        if isinstance(is_flightless, bool):
            self.__is_flightless = is_flightless

    # --------------------
    # Property definitions
    # --------------------

    is_flightless = property(get_is_flightless, set_is_flightless)

    # -------------------
    # Behavioural methods
    # -------------------

    def make_sound(self):
        print(f"{self.name} the {self.species} is tweeting and chirping.")

    def eat(self):
        print(f"{self.name} the {self.species} is now pecking at their {self.dietary_requirements}.")

    def sleep(self):
        print(f"{self.name} the {self.species} is now sleeping in its nest or perch.")

    def move(self):
        move = 'flying'
        if self.is_flightless:
            move = 'walking'
        return f"{self.name} the {self.species} is {move} around the enclosure."

    def lay_eggs(self):
        if self.is_female:
            return f"{self.name} the {self.species} has laid eggs."
        else:
            return f"{self.name} cannot lay eggs because they are male."

    def __str__(self):
        if self.is_flightless:
            flight = 'This bird is flightless.\n'
        else:
            flight = 'This bird can fly.\n'
        return super().__str__() + flight


class Reptile(Animal):
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
