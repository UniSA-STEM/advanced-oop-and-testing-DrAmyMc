"""
File: staff.py
Description: Abstract 'Staff' class and its concrete subclasses, for use in a Zoo.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from enclosure import Enclosure


class Staff:
    """
    Represents an employee at the zoo. Subclasses exist for specialised employee types.
    """
    def __init__(self, staff_id, first_name, last_name, year_hired):
        """
        Initialises a new Staff instance.

        Args:
            staff_id (int): The ID of the employee at the zoo.
            first_name (str): The employee's first name.
            last_name (str): The employee's last name.
            year_hired (int): The year the employee was hired.

        Attributes:
            __staff_id (int): The ID of the employee at the zoo.
            __first_name (str): The employee's first name.
            __last_name (str): The employee's last name.
            __year_hired (int): The year the employee was hired.
            __role (str): The role that the employee has been hired to fill.
            __responsibilities (list): List of the employee's responsibilities.
        """
        self.staff_id = staff_id                #Utilises the setter for validation of new instances
        self.first_name = first_name            #Utilises the setter for validation of new instances
        self.last_name = last_name              #Utilises the setter for validation of new instances
        self.year_hired = year_hired            #Utilises the setter for validation of new instances
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

    def get_year_hired(self)->int:
        """Returns the year the employee was hired ."""
        return self.__year_hired

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
        Args: staff_id (int): The staff id number.
        """
        MIN = 100000
        MAX = 999999
        if isinstance(staff_id, int) and MIN <= staff_id <= MAX:
            self.__staff_id = staff_id
        else:
            print(f"Invalid staff id number. Please enter an integer between {MIN_LEVEL} and {MAX_LEVEL}.")

    def set_first_name(self, first_name):
        """
        Sets the employee's first name.
        Args: first_name (str): The employee's first name, ensuring only a string of a minimum length may be passed.
        """
        MIN_LENGTH = 2
        if isinstance(first_name, str) and len(first_name) >= MIN_LENGTH:
            self.__first_name = first_name
        else:
            print(f"Invalid employee first name. Please enter text of at least {MIN_LENGTH} characters.")

    def set_last_name(self, last_name):
        """
        Sets the employee's last name.
        Args: last_name (str): The employee's last name, ensuring only a string of a minimum length may be passed.
        """
        MIN_LENGTH = 2
        if isinstance(last_name, str) and len(last_name) >= MIN_LENGTH:
            self.__last_name = last_name
        else:
            print(f"Invalid employee last name. Please enter text of at least {MIN_LENGTH} characters.")

    def set_year_hired(self, year_hired):
        """
        Updates the year hired, ensuring it remains within a valid range.
        Args: year_hired (int): The year hired.
        """
        MIN_YEAR = 2010
        MAX_YEAR = 2050
        if isinstance(year_hired, int) and MIN_YEAR <= year_hired <= MAX_YEAR:
            self.__year_hired = year_hired
        else:
            print(f"Please enter a valid year between {MIN_YEAR} and {MAX_YEAR}.")

    def set_role(self, role):
        """
        Sets the employee's role.
        Args: role (str): The employee's role, ensuring only a string of a minimum length may be passed.
        """
        MIN_LENGTH = 4
        if isinstance(role, str) and len(role) >= MIN_LENGTH:
            self.__role = role
        else:
            print(f"Invalid employee role. Please enter text of at least {MIN_LENGTH} characters.")

    # --------------------
    # Property definitions
    # --------------------

    staff_id = property(get_staff_id, set_staff_id)
    first_name = property(get_first_name, set_first_name)
    last_name = property(get_last_name, set_last_name)
    year_hired = property(get_year_hired, set_year_hired)
    role = property(get_role, set_role)
    responsibilities = property(get_responsibilities)
    assigned_enclosures = property(get_assigned_enclosures)

    # -------------------
    # Behavioural methods
    # -------------------

    def __str__(self):
        """
        Returns a formatted string containing the employee's details.
        Returns: str: The name, year hired, and role.
        """
        try:
            responsibilities_str = ""
            assigned_enclosures_str = ""
            if self.responsibilities != []:
                responsibilities_str = 'Responsibilities:\n'
                for responsibility in self.responsibilities:
                    responsibilities_str += f"   {responsibility}\n"
            if self.assigned_enclosures != []:
                assigned_enclosures_str = 'Assigned Enclosures:\n'
                for enclosure in self.assigned_enclosures:
                    assigned_enclosures_str += "   {enclosure}\n"
            return (f"{self.first_name} {self.last_name} was hired in {self.year_hired} in the role of {self.role}.\n"
                    + responsibilities_str + assigned_enclosures_str)
        except:
            return f"Invalid object.\n"

    # -------------------
    # Behavioural methods
    # -------------------

    def assign_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            self.__assigned_enclosures.append(enclosure)


class Veterinarian(Staff):
    def __init__(self, staff_id, first_name, last_name, year_hired):
        super().__init__(staff_id, first_name, last_name, year_hired)
        self._responsibilities = ['Conduct health checks', 'Treat animals', 'Plan preventive health care']

    # -------------------
    # Behavioural methods
    # -------------------

    def conduct_health_check(self, animal):
        pass

    def add_health_record(self, issue_type, severity_level, date_reported, description, treatment_plan):
        """
        Initialises a new Health Record instance for the animal.

        Args:
            issue_type (str): The category of issue being reported.
            severity_level (int): The severity level from 0-3.
            date_reported (str): The date of the initial report.
            description (str): A description of the health issue
            treatment_plan (str): The initial treatment plan/notes.
        """
        new_record = HealthRecord(issue_type, severity_level, date_reported, description, treatment_plan)
        self.health_record.append(new_record)
        print(f"New health record created:\n"
              f"{new_record}")


class Zookeeper(Staff):
    def __init__(self, staff_id, first_name, last_name, year_hired):
        super().__init__(staff_id, first_name, last_name, year_hired)
        self._responsibilities = ['Feed animals', 'Clean enclosures', 'Exhibit planning']

    # -------------------
    # Behavioural methods
    # -------------------

    def clean_enclosure(self, enclosure_name):
        pass

    def feed_animals(self, species):
        pass
