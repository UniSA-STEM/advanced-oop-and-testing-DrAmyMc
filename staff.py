"""
File: staff.py
Description: 'Staff' parent class, for use in a Zoo.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from datetime import datetime
from enclosure import Enclosure


class Staff:
    """
    Represents an employee at the zoo. Subclasses exist for specialised employee types, such as
    zookeeper and veterinarian.

    Attributes:
        staff_id (int): The ID of the employee at the zoo.
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
        date_hired (date): The date the employee was hired.
        role (str): The role that the employee has been hired to fill.
        responsibilities (list): List of the employee's responsibilities.
        assigned_enclosures (list): List of enclosure's assigned to the employee.
    """
    def __init__(self, staff_id, first_name, last_name, date_hired):
        """
        Initialises a new Staff instance.

        Args:
            staff_id (int): The ID of the employee at the zoo.
            first_name (str): The employee's first name.
            last_name (str): The employee's last name.
            date_hired (str): The date the employee was hired dd/mm/yyyy.
        """
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_hired = date_hired
        self.__role = self.__class__.__name__   #Utilises the name of the class to label the role
        self._responsibilities = []
        self.__assigned_enclosures = []

    # --------------
    # Getter methods
    # --------------

    def get_staff_id(self)->int:
        """Return's the employee's staff ID number."""
        return self.__staff_id

    def get_first_name(self)->str:
        """Returns the employee's first name."""
        return self.__first_name

    def get_last_name(self)->str:
        """Returns the employee's last name."""
        return self.__last_name

    def get_date_hired(self)->datetime:
        """Returns the date the employee was hired ."""
        return self.__date_hired

    def get_role(self)->str:
        """Returns the employee's role."""
        return self.__role

    def get_responsibilities(self)->list:
        """Returns a list of the employee's responsibilities."""
        return self._responsibilities

    def get_assigned_enclosures(self)->list:
        """Returns a list of the enclosures assigned to the employee."""
        return self.__assigned_enclosures

    # --------------
    # Setter methods
    # --------------

    def set_staff_id(self, staff_id):
        """
        Sets the staff id number, ensuring it is a valid id number.
        Args: staff_id (int): The staff id number of 6 digits.
        """
        MIN = 100000
        MAX = 999999
        if isinstance(staff_id, int) and MIN <= staff_id <= MAX:
            self.__staff_id = staff_id
        else:
            raise ValueError(f"Invalid staff id number. Please enter an integer between {MIN} and {MAX}.")

    def set_first_name(self, first_name):
        """
        Sets the employee's first name.
        Args: first_name (str): The employee's first name, ensuring only a string of a minimum length may be passed.
        """
        MIN_LENGTH = 2
        if isinstance(first_name, str) and len(first_name) >= MIN_LENGTH:
            self.__first_name = first_name
        else:
            raise ValueError(f"Invalid employee first name. Please enter text of at least {MIN_LENGTH} characters.")

    def set_last_name(self, last_name):
        """
        Sets the employee's last name.
        Args: last_name (str): The employee's last name, ensuring only a string of a minimum length may be passed.
        """
        MIN_LENGTH = 2
        if isinstance(last_name, str) and len(last_name) >= MIN_LENGTH:
            self.__last_name = last_name
        else:
            raise ValueError(f"Invalid employee last name. Please enter text of at least {MIN_LENGTH} characters.")

    def set_date_hired(self, date_hired):
        """
        Set the date the employee was hired in date format.
        Args: date_hired (str): The date the employee was hired as a string (dd/mm/yyyy)..
        """
        try:
            self.__date_hired = datetime.strptime(date_hired, "%d/%m/%Y").date()
        except:
            raise ValueError(f"Invalid date reported. Must be in format dd/mm/yyyy.")

    def set_role(self, role):
        """
        Sets the employee's role.
        Args: role (str): The employee's role, ensuring only a string of a minimum length may be passed.
        """
        MIN_LENGTH = 4
        if isinstance(role, str) and len(role) >= MIN_LENGTH:
            self.__role = role
        else:
            raise ValueError(f"Invalid employee role. Please enter text of at least {MIN_LENGTH} characters.")

    # --------------------
    # Property definitions
    # --------------------

    staff_id = property(get_staff_id, set_staff_id)
    first_name = property(get_first_name, set_first_name)
    last_name = property(get_last_name, set_last_name)
    date_hired = property(get_date_hired, set_date_hired)
    role = property(get_role, set_role)
    responsibilities = property(get_responsibilities)
    assigned_enclosures = property(get_assigned_enclosures)

    # -------------------
    # Helper methods
    # -------------------

    def search_assigned_enclosures(self, enclosure_name)-> object | None:
        """Returns the assigned enclosure if found in the assigned enclosure list, otherwise None."""
        for enclosure in self.assigned_enclosures:
            if enclosure.name == enclosure_name:
                return enclosure

    # -------------------
    # Behavioural methods
    # -------------------

    def assign_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            self.__assigned_enclosures.append(enclosure)

    def __str__(self):
        """
        Returns a formatted string containing the employee's details.
        Returns: str: The staff ID, name, date hired, and role.
        """
        details = [f"{self.first_name} {self.last_name} was hired on {self.date_hired} in the role of {self.role}."]
        if self.responsibilities != []:
            details.append('---Responsibilities---')
            for responsibility in self.responsibilities:
                details.append(responsibility)
        if self.assigned_enclosures != []:
            details.append('---Assigned Enclosures---')
            for enclosure in self.assigned_enclosures:
                details.append(enclosure)
        details.append("")
        return '\n'.join(details)
