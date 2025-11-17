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