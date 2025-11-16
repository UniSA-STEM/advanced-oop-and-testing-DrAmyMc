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
    def __init__(self, name, age, is_female, species, fur_type):
        super().__init__(name, age, is_female, species)
        self.fur_type = fur_type
        self.__is_pregnant = False

    # --------------
    # Getter methods
    # --------------

    def get_fur_type(self)->str:
        """Returns the animal's fur type."""
        return self.__fur_type

    def get_is_pregnant(self)->bool:
        """Returns the animal's pregnancy status - True or False."""
        return self.__is_pregnant

    # --------------
    # Setter methods
    # --------------

    def set_fur_type(self, fur_type):
        """
                Updates the date of the report.

                Args:
                    date_reported (str): The date that the issue was reported, ensuring only a string of a minimum
                    length may be passed.
                """
        MIN_LENGTH = 3
        if isinstance(fur_type, str) and len(fur_type) >= MIN_LENGTH:
            self.__fur_type = fur_type
        else:
            print(f"Invalid fur type. Please enter text of at least {MIN_LENGTH} characters.")

    def set_is_pregnant(self, is_pregnant):
        """
        Sets the pregnancy status of the mammal.

        Args:
            is_pregnant (bool): True if pregnant, False if not pregnant. Must be boolean.
        """
        if isinstance(is_pregnant, bool) and self.is_female:
            self.__is_pregnant = is_pregnant
        elif not self.is_female:
            print(f"Invalid - male animal cannot be pregnant.")
        else:
            print(f"Invalid value. Please enter True if pregnant or False if not pregnant.")

    # --------------------
    # Property definitions
    # --------------------

    fur_type = property(get_fur_type, set_fur_type)
    is_pregnant = property(get_is_pregnant, set_is_pregnant)

    # -------------------
    # Behavioural methods
    # -------------------

    def make_sound(self):
        return f"{self.name} the {self.species} is making mammal noises."

    def eat(self):
        return f"{self.name} the {self.species} is eating their {self.dietary_requirements}."

    def sleep(self):
        return f"{self.name} the {self.species} is sleeping."

    def move(self):
        return f"{self.name} the {self.species} is walking around their enclosure."

    def __str__(self):
        try:
            if not self.is_female:
                pregnant = ''
            else:
                pregnant = 'Pregnancy status: PREGNANT\n' if self.is_pregnant else 'Pregnancy status: Not pregnant\n'
            return super().__str__() + f"\nFur type: {self.fur_type}" + f"\n{pregnant}"
        except:
            return "Invalid object.\n"


class Bird(Animal):
    def __init__(self, name, age, is_female, species, wingspan, is_flightless):
        super().__init__(name, age, is_female, species)
        self.wingspan = wingspan
        self.is_flightless = is_flightless

    # --------------
    # Getter methods
    # --------------

    def get_wingspan(self)->int:
        """Returns the bird's wingspan in metres."""
        return self.__wingspan

    def get_is_flightless(self)->bool:
        """Returns whether the bird is flightless."""
        return self.__is_flightless

    # --------------
    # Setter methods
    # --------------

    def set_wingspan(self, wingspan):
        """
        Sets the wingspan, ensuring it remains within a valid range.

        Args:
            wingspan (float): The wingspan in metres
        """
        MIN_SPAN = 0.03
        MAX_SPAN = 3.70
        if isinstance(wingspan, float) and MIN_SPAN <= wingspan <= MAX_SPAN:
            self.__wingspan = wingspan
        else:
            print(f"Invalid wingspan. Please enter the wingspan in metres between {MIN_LEVEL} and {MAX_LEVEL}.")

    def set_is_flightless(self, is_flightless):
        """
       Sets whether the bird is flightless.

       Args:
           is_flightless (bool): True if flightless, False if able to fly. Must be boolean.
       """
        if isinstance(is_flightless, bool):
            self.__is_flightless = is_flightless
        else:
            print(f"Invalid value. Please enter True if flightless or False if able to fly.")

    # --------------------
    # Property definitions
    # --------------------

    wingspan = property(get_wingspan, set_wingspan)
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
        try:
            flight = 'This bird is flightless.\n' if self.is_flightless else 'This bird can fly.\n'
            return super().__str__() + f"\nWingspan: {self.wingspan}m\n" + flight
        except:
            return "Invalid object.\n"


class Reptile(Animal):
    def __init__(self, name, age, is_female, species, min_temp, is_venomous):
        super().__init__(name, age, is_female, species)
        self.min_temp = min_temp
        self.is_venomous = is_venomous

    # --------------
    # Getter methods
    # --------------

    def get_min_temp(self)->int:
        """Returns the minimum temperature required by the reptile."""
        return self.__min_temp

    def get_is_venomous(self)->bool:
        """Returns whether the reptile is venomous."""
        return self.__is_venomous

    # --------------
    # Setter methods
    # --------------

    def set_min_temp(self, min_temp):
        """
        Updates the minimum temperature, ensuring it is a valid value.

        Args:
            min_temp (int): The min temp in degrees C.
        """
        MIN_TEMP = 15
        MAX_TEMP = 25
        if isinstance(min_temp, int) and MIN_TEMP <= min_temp <= MAX_TEMP:
            self.__min_temp = min_temp
        else:
            print(f"Invalid temperature. Please enter a integer between {MIN_TEMP} and {MAX_TEMP}.")

    def set_is_venomous(self, is_venomous):
        """
       Sets whether the reptile is venomous.

       Args:
           is_venomous (bool): True if venomous, False if not. Must be boolean.
       """
        if isinstance(is_venomous, bool):
            self.__is_venomous = is_venomous
        else:
            print(f"Invalid value. Please enter True if venomous or False if not venomous.")

    # --------------------
    # Property definitions
    # --------------------

    min_temp = property(get_min_temp, set_min_temp)
    is_venomous = property(get_is_venomous, set_is_venomous)

    # -------------------
    # Behavioural methods
    # -------------------

    def make_sound(self):
        return f"{self.name} the {self.species} is making reptile noises."

    def eat(self):
        return f"{self.name} the {self.species} is eating {self.dietary_requirements}."

    def sleep(self):
        return f"{self.name} the {self.species} is sleeping."

    def move(self):
        return f"{self.name} the {self.species} is moving about their enclosure."

    def lay_eggs(self):
        if self.is_female:
            return f"{self.name} the {self.species} has laid eggs."
        else:
            return f"{self.name} cannot lay eggs because they are male."

    def __str__(self):
        try:
            venomous = 'Handle with care - venomous.\n' if self.is_venomous else 'Safe to handle - not venomous.\n'
            return super().__str__() + f"\nMinimum temperature: {self.min_temp}\u00b0C\n" + venomous
        except:
            return "Invalid object.\n"