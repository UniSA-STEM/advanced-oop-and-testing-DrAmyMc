"""
File: bird.py
Description: Bird subclass of abstract Animal class for use in a Zoo.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal


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

    def make_sound(self)->str:
        return f"{self.name} the {self.species} is tweeting and chirping."

    def eat(self)->str:
        return f"{self.name} the {self.species} is now pecking at their {self.dietary_requirements}."

    def sleep(self)->str:
        return f"{self.name} the {self.species} is now sleeping in its nest or perch."

    def move(self)->str:
        move = 'flying'
        if self.is_flightless:
            move = 'walking'
        return f"{self.name} the {self.species} is {move} around the enclosure."

    def lay_eggs(self)->str:
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