"""
File: mammal.py
Description: Mammal subclass of abstract Animal class for use in a Zoo.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal


class Mammal(Animal):
    """Represents a Mammal type of Animal with mammal-specific features."""

    def __init__(self, name, age, is_female, species, fur_type):
        """
        Initialises a new Mammal instance of the Mammal subclass.

        Args:
            name (str): The name of the animal.
            age (int): The age of the animal.
            is_female (bool): The sex of the animal.
            species (str): The species of the animal.
            fur_type (str): The fur type of the mammal.

        Attributes:
            __name (str): The animal's name.
            __age (int): The animal's age.
            __is_female (bool): The animal's sex (True if female, False if male)
            __species (str): The species of animal.
            __is_native (bool): Whether the animal species is native to Australia.
            __dietary_requirements (str): The diet of the animal species.
            __environment (str): The environment requirement of the animal species.
            __space (str): The amount of space required per animal of that animal species.
            __health_record (list): List of health records for the animal.
            __fur_type (str): The mammal's fur type.
            __is_pregnant (bool): The mammal's pregnancy status.
        """
        # User inputs for name, age, is_female, and species come from parent class
        super().__init__(name, age, is_female, species)
        self.fur_type = fur_type  # User input for fur_type utilises setter for validation
        self.__is_pregnant = False  # False by default

    # --------------
    # Getter methods
    # --------------

    def get_fur_type(self) -> str:
        """Returns the animal's fur type."""
        return self.__fur_type

    def get_is_pregnant(self) -> bool:
        """Returns the animal's pregnancy status - True or False."""
        return self.__is_pregnant

    # --------------
    # Setter methods
    # --------------

    def set_fur_type(self, fur_type):
        """
        Sets the animal's fur type.
        Args: fur_type (str): The animal's fur type, ensuring only a string of a min length may be passed.
        """
        MIN_LENGTH = 3
        if isinstance(fur_type, str) and len(fur_type) >= MIN_LENGTH:
            self.__fur_type = fur_type
        else:
            raise ValueError(f"Invalid fur type. Please enter text of at least {MIN_LENGTH} characters.")

    def set_is_pregnant(self, is_pregnant):
        """
        Sets the pregnancy status of the mammal.
        Args: is_pregnant (bool): True if pregnant, False if not pregnant. Must be boolean.
        """
        if isinstance(is_pregnant, bool) and self.is_female:
            self.__is_pregnant = is_pregnant
        elif not self.is_female:
            raise ValueError(f"Invalid - male animal cannot be pregnant.")
        else:
            raise ValueError(f"Invalid value. Please enter True if pregnant or False if not pregnant.")

    # --------------------
    # Property definitions
    # --------------------

    fur_type = property(get_fur_type, set_fur_type)
    is_pregnant = property(get_is_pregnant, set_is_pregnant)

    # -------------------
    # Behavioural methods
    # -------------------

    def make_sound(self):
        """Returns the mammal making a sound."""
        return f"{self.name} the {self.species} makes low, rich mammalian noises."

    def eat(self):
        """Returns the mammal eating."""
        return f"{self.name} the {self.species} chews on their {self.dietary_requirements}."

    def sleep(self):
        """Returns the mammal sleeping."""
        return f"{self.name} the {self.species} curls up and goes to sleep."

    def move(self):
        """Returns the mammal moving"""
        return f"{self.name} the {self.species} roams around their {self.environment.lower()} enclosure."

    def __str__(self) -> str:
        """
        Returns a formatted string containing the animal's details.
        Returns: str: The animal class string plus mammal-specific fur type and pregnancy status details.
        """
        if not self.is_female:
            pregnant = ''
        else:
            pregnant = 'Pregnancy status: PREGNANT\n' if self.is_pregnant else 'Pregnancy status: Not pregnant\n'
        return super().__str__() + f"Fur type: {self.fur_type}" + f"\n{pregnant}"
