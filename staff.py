"""
File: staff.py
Description: Abstract 'Staff' class and its concrete subclasses, for use in a Zoo.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod


class Staff(ABC):
    def __init__(self, name, year_hired):
        self.name = name
        self.year_hired = year_hired
        self.__role = self.__class__.__name__

    # --------------
    # Getter methods
    # --------------

    def get_name(self)->str:
        """Returns the employee's name."""
        return self.__name

    def get_year_hired(self)->int:
        """Returns the year the employee was hired ."""
        return self.__year_hired

    def get_role(self)->str:
        """Returns the employee's role."""
        return self.__role

    # --------------
    # Setter methods
    # --------------

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def set_year_hired(self, year_hired):
        if isinstance(year_hired, int) and 2010 <= year_hired <= 2050:
            self.__year_hired = year_hired

    # --------------------
    # Property definitions
    # --------------------

    name = property(get_name, set_name)
    year_hired = property (get_year_hired, set_year_hired)
    role = property(get_role)

    # -------------------
    # Behavioural methods
    # -------------------

    def __str__(self):
        return f"{self.name} was hired in {self.year_hired} in the role of {self.role}."

    # -----------------
    # Abstract methods
    # -----------------

    @abstractmethod
    def method(self):
        pass


class Veterinarian(Staff):
    def __init__(self, name, year_hired):
        super().__init__(name, year_hired)

    # -------------------
    # Behavioural methods
    # -------------------

    def method(self):
        pass

class Zookeeper(Staff):
    def __init__(self, name, year_hired):
        super().__init__(name, year_hired)

    # -------------------
    # Behavioural methods
    # -------------------

    def method(self):
        pass
