"""
File: reptile.py
Description: Reptile subclass of abstract Animal class for use in a Zoo.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal


class Reptile(Animal):
    """A reptile with min temperature and venomous status, extending Animal."""

    def __init__(self, name, age, is_female, species, min_temp, is_venomous):
        """
        Initialises a new Reptile instance of the Reptile subclass.

        Args:
            min_temp (int): The minimum temperature required by the reptile in degrees Celsius.
            is_venomous (bool): The venomous state of the reptile.

         Notes: Other attributes such as name, age, species, etc. are initialised by the parent class.
        """
        super().__init__(name, age, is_female, species)
        self.min_temp = min_temp
        self.is_venomous = is_venomous

    # --------------
    # Getter methods
    # --------------

    def get_min_temp(self) -> int:
        """Returns the minimum temperature required by the reptile."""
        return self.__min_temp

    def get_is_venomous(self) -> bool:
        """Returns whether the reptile is venomous."""
        return self.__is_venomous

    # --------------
    # Setter methods
    # --------------

    def set_min_temp(self, min_temp):
        """
        Sets the minimum temperature, ensuring it is a valid value.
        Args: min_temp (int): The min temp in degrees C.
        """
        MIN_TEMP = 15
        MAX_TEMP = 25
        if type(min_temp) is int and MIN_TEMP <= min_temp <= MAX_TEMP:
            self.__min_temp = min_temp
        else:
            raise ValueError(f"Invalid temperature. Please enter a integer between {MIN_TEMP} and {MAX_TEMP}.")

    def set_is_venomous(self, is_venomous):
        """
        Sets whether the reptile is venomous.
        Args: is_venomous (bool): True if venomous, False if not. Must be boolean.
        """
        if type(is_venomous) is bool:
            self.__is_venomous = is_venomous
        else:
            raise ValueError(f"Invalid value. Please enter True if venomous or False if not venomous.")

    # --------------------
    # Property definitions
    # --------------------

    min_temp = property(get_min_temp, set_min_temp)
    is_venomous = property(get_is_venomous, set_is_venomous)

    # -------------------
    # Behavioural methods
    # -------------------

    def make_sound(self) -> str:
        """Returns the reptile making a sound."""
        return f"{self.name} the {self.species} makes a soft reptilian sound."

    def eat(self) -> str:
        """Returns the reptile eating."""
        return f"{self.name} the {self.species} slowly feeds on their {self.dietary_requirements}."

    def sleep(self) -> str:
        """Returns the reptile sleeping."""
        return f"{self.name} the {self.species} becomes still and rests in a sheltered spot."

    def move(self) -> str:
        """Returns the reptile moving."""
        return f"{self.name} the {self.species} moves slowly about their {self.environment.lower()} enclosure."

    def bask(self) -> str:
        """Returns the reptile basking."""
        return f"{self.name} the {self.species} basks in the heat to warm their core temperature."

    def lay_eggs(self) -> str:
        if self.is_female:
            return f"{self.name} the {self.species} lays eggs."
        else:
            return f"{self.name} cannot lay eggs because he is male."

    # --------------
    # String display
    # --------------

    def __str__(self) -> str:
        """
        Returns a formatted string containing the animal's details.
        Returns: str: The animal class string plus reptile-specific min temp and venomous details.
        """
        venomous = 'Handle with care - VENOMOUS.\n' if self.is_venomous else 'Safe to handle - not venomous.\n'
        return super().__str__() + f"Minimum temperature: {self.min_temp}\u00b0C\n" + venomous
