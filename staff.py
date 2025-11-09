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
    """
    Represents an employee at the zoo in the abstract sense.
    """

    def __init__(self, name, year_hired):
        """
           Initialises a new Staff instance when utilised through a concrete subclass.

           Args:
               name (str): The employee's name.
               year_hired (int): The year the employee was hired.

           Attributes:
               __name (str): The employee's name.
               __year_hired (int): The year the employee was hired.
               __role (str): The role that the employee has been hired to fill.
        """
        self.name = name                        #Utilises the setter for validation of new instances
        self.year_hired = year_hired            #Utilises the setter for validation of new instances
        self.__role = self.__class__.__name__   #Utilises the name of the class to label the role

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
        """
        Updates the employee's name.

        Args:
            name (str): The new name for the employee, ensuring only a string may be passed.
        """
        if isinstance(name, str):
            self.__name = name

    def set_year_hired(self, year_hired):
        """
            Updates the year hired, ensuring it remains within a valid range.

            Args:
                year_hired (int): The new year hired.
            """
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
        """
        Returns a formatted string containing the employee's details.

        Returns:
            str: The name, year hired, and role.
        """
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
