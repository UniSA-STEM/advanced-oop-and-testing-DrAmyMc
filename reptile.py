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

    def make_sound(self)->str:
        return f"{self.name} the {self.species} is making reptile noises."

    def eat(self)->str:
        return f"{self.name} the {self.species} is eating {self.dietary_requirements}."

    def sleep(self)->str:
        return f"{self.name} the {self.species} is sleeping."

    def move(self)->str:
        return f"{self.name} the {self.species} is moving about their enclosure."

    def lay_eggs(self)->str:
        if self.is_female:
            return f"{self.name} the {self.species} has laid eggs."
        else:
            return f"{self.name} cannot lay eggs because they are male."

    def __str__(self)->str:
        try:
            venomous = 'Handle with care - venomous.\n' if self.is_venomous else 'Safe to handle - not venomous.\n'
            return super().__str__() + f"\nMinimum temperature: {self.min_temp}\u00b0C\n" + venomous
        except:
            return "Invalid object.\n"