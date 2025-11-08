'''
File: staff.py
Description: A brief description of this Python module.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

class Staff(ABC):
    def __init__(self, name, year_hired):
        self.name = name
        self.year_hired = year_hired
        self.__role = self.__class__.__name__

    def get_name(self):
        return self.__name

    def get_year_hired(self):
        return self.__year_hired

    def get_role(self):
        return self.__role

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def set_year_hired(self, year_hired):
        if isinstance(year_hired, int) and 2010 <= year_hired <= 2050:
            self.__year_hired = year_hired

    name = property(get_name, set_name)
    year_hired = property (get_year_hired, set_year_hired)
    role = property(get_role)

    @abstractmethod
    def method(self):
        pass

    def __str__(self):
        return f"{self.name} was hired in {self.year_hired} in the role of {self.role}."

class Veterinarian(Staff):
    def __init__(self, name, year_hired):
        super().__init__(name, year_hired)

    def method(self):
        pass

class Zookeeper(Staff):
    def __init__(self, name, year_hired):
        super().__init__(name, year_hired)

    def method(self):
        pass

