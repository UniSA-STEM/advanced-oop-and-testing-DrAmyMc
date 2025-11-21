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
    """A bird with wingspan and flight ability, extending Animal."""

    def __init__(self, name, age, is_female, species, wingspan, is_flightless):
        """
        Initialises a new Bird instance of the Bird subclass.

        Args:
            wingspan (float): The wingspan of the bird in metres.
            is_flightless (bool): The flightless state of the bird.

         Notes: Other attributes such as name, age, species, etc. are initialised by the parent class.
        """
        super().__init__(name, age, is_female, species)
        self.wingspan = wingspan
        self.is_flightless = is_flightless

    # --------------
    # Getter methods
    # --------------

    def get_wingspan(self) -> int:
        """Returns the bird's wingspan in metres."""
        return self.__wingspan

    def get_is_flightless(self) -> bool:
        """Returns whether the bird is flightless."""
        return self.__is_flightless

    # --------------
    # Setter methods
    # --------------

    def set_wingspan(self, wingspan):
        """
        Sets the wingspan, ensuring it remains within a valid range.
        Args: wingspan (int | float): The wingspan in metres
        """
        MIN_SPAN = 0.03
        MAX_SPAN = 3.7
        if (type(wingspan) is float or type(wingspan) is int) and MIN_SPAN <= wingspan <= MAX_SPAN:
            self.__wingspan = float(wingspan)
        else:
            raise ValueError(f"Invalid wingspan. Please enter the wingspan in metres between "
                             f"{MIN_SPAN} and {MAX_SPAN}.")

    def set_is_flightless(self, is_flightless):
        """
        Sets whether the bird is flightless.
        Args: is_flightless (bool): True if flightless, False if able to fly. Must be boolean.
        """
        if type(is_flightless) is bool:
            self.__is_flightless = is_flightless
        else:
            raise ValueError(f"Invalid value. Please enter True if flightless or False if able to fly.")

    # --------------------
    # Property definitions
    # --------------------

    wingspan = property(get_wingspan, set_wingspan)
    is_flightless = property(get_is_flightless, set_is_flightless)

    # -------------------
    # Behavioural methods
    # -------------------

    def make_sound(self) -> str:
        """Returns the bird making a sound."""
        return f"{self.name} the {self.species} makes a bird call."

    def eat(self) -> str:
        """Returns the bird eating."""
        return f"{self.name} the {self.species} pecks at their {self.dietary_requirements}."

    def sleep(self) -> str:
        """Returns the bird sleeping."""
        return f"{self.name} the {self.species} roosts and goes to sleep."

    def move(self) -> str:
        """Returns the bird moving."""
        move = 'walks' if self.is_flightless else 'flies'
        return f"{self.name} the {self.species} {move} around their {self.environment.lower()} enclosure."

    def lay_eggs(self) -> str:
        """Returns the bird laying eggs if female, error message if male."""
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
        Returns: str: The animal class string plus bird-specific wingspan and flightless status details.
        """
        flight = 'This bird is flightless.\n' if self.is_flightless else 'This bird can fly.\n'
        return super().__str__() + f"Wingspan: {self.wingspan}m\n" + flight
