"""
File: healthrecord.py
Description: Health Record class, to be associated with an animal object.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from datetime import datetime


class HealthRecord:
    """
    Represents a health record for an animal.
    The Health Record class models a single instance for a single animal, to be attached to that animals
    health history.

    Attributes:
        issue_type (str): The category of issue being reported.
        severity_level (int): The severity level from 0-3 (Negligible, Minor, Moderate, Severe).
        date_reported (date): The date of the initial report.
        description (str): Description of the health issue.
        treatment_plan (list): Treatment plan and notes, including subsequent updates.
        is_current (bool): If the issue is current.
        treating_vet (str): The vet treating the animal
    """

    # Three categories for health issues recorded
    ISSUE_TYPE = ['Injury', 'Illness', 'Behavioural Issue']

    def __init__(self, issue_type, severity_level, date_reported, description, treatment_plan, vet_name):
        """
        Initialises a new Health Record instance.

        Args:
            issue_type (str): The category of issue being reported.
            severity_level (int): The severity level from 0-3.
            date_reported (str): The date of the initial report.
            description (str): A description of the health issue
            treatment_plan (str): The initial treatment plan/notes.
            vet_name (str): The name of the treating vet.
        """
        self.issue_type = issue_type
        self.severity_level = severity_level
        self.date_reported = date_reported
        self.description = description
        self.treatment_plan = treatment_plan
        self.is_current = True
        self.treating_vet = vet_name

    # --------------
    # Getter methods
    # --------------

    def get_issue_type(self)->str:
        """Returns the health issue type."""
        return self.__issue_type

    def get_severity_level(self)->int:
        """Returns the severity level of the health issue."""
        return self.__severity_level

    def get_date_reported(self)->datetime:
        """Returns the date that the health issue was reported."""
        return self.__date_reported

    def get_description(self)->str:
        """Returns a description of the health issue."""
        return self.__description

    def get_treatment_plan(self)->list:
        """Returns the list of treatment plan notes."""
        return self.__treatment_plan

    def get_is_current(self) -> bool:
        """Returns whether the health issue is current (True) or resolved (False)."""
        return self.__is_current

    def get_treating_vet(self)->str:
        """Returns the name of the treating vet."""
        return self.__treating_vet

    # --------------
    # Setter methods
    # --------------

    def set_issue_type(self, issue_type):
        """
        Sets the health issue type.
        Args: type (str): The type of health issue being recorded. Must be a valid type.
        """
        if issue_type in HealthRecord.ISSUE_TYPE:
            self.__issue_type = issue_type
        else:
            raise ValueError(f"Invalid issue type. Please enter one of the following types:\n"
                  f"{HealthRecord.ISSUE_TYPE}")

    def set_severity_level(self, level):
        """
        Updates the severity level, ensuring it remains within a valid range.
        Args: severity_level (int): The new severity level (0-3).
        """
        MIN_LEVEL = 0
        MAX_LEVEL = 3
        if isinstance(level, int) and MIN_LEVEL <= level <= MAX_LEVEL:
            self.__severity_level = level
        else:
            raise ValueError(f"Invalid severity level. Please enter an integer between {MIN_LEVEL} and {MAX_LEVEL}.")

    def set_date_reported(self, date_reported):
        """
        Sets the date of the report in date format.
        Args: date_reported (str): The date that the issue was reported as a string (dd/mm/yyyy).
        """
        try:
            self.__date_reported = datetime.strptime(date_reported, "%d/%m/%Y").date()
        except:
            raise ValueError(f"Invalid date reported. Must be in format dd/mm/yyyy.")

    def set_description(self, description):
        """
        Sets the description of the health issue.
        Args: description (str): Description of the health issue, with a string of min length.
        """
        MIN_LENGTH = 6
        if isinstance(description, str) and len(description) >= MIN_LENGTH:
            self.__description = description
        else:
            raise ValueError(f"Invalid description. Please enter text of at least {MIN_LENGTH} characters.")

    def set_treatment_plan(self, treatment_plan):
        """
        Sets the initial treatment plan/notes.
        Args: treatment_plan (str): The treatment plan/notes for the health issue, ensuring only a string
             of a minimum length may be passed.
        """
        MIN_LENGTH = 6
        if isinstance(treatment_plan, str) and len(treatment_plan) >= MIN_LENGTH:
            self.__treatment_plan = [treatment_plan]
        else:
            raise ValueError(f"Invalid treatment plan. Please enter text of at least {MIN_LENGTH} characters.")

    def set_is_current(self, is_current):
        """
        Sets the status of the health issue (current = True, resolved = False).
        Args: is_current (bool): The status of the health issue.
        """
        if isinstance(is_current, bool):
            self.__is_current = is_current
        else:
            raise ValueError(f"Invalid current health status. Please enter either True (issue still current) or "
                  f"False (issue resolved).")

    def set_treating_vet(self, vet_name):
        """
        Sets the description of the health issue.
        Args: description (str): Description of the health issue, with a string of min length.
        """
        MIN_LENGTH = 5
        if isinstance(vet_name, str) and len(vet_name) >= MIN_LENGTH:
            self.__treating_vet = vet_name
        else:
            raise ValueError(f"Invalid vet name. Please enter text of at least {MIN_LENGTH} characters.")

    # --------------------
    # Property definitions
    # --------------------

    issue_type = property(get_issue_type, set_issue_type)
    severity_level = property(get_severity_level, set_severity_level)
    date_reported = property(get_date_reported, set_date_reported)
    description = property(get_description, set_description)
    treatment_plan = property(get_treatment_plan, set_treatment_plan)
    is_current = property(get_is_current, set_is_current)
    treating_vet = property(get_treating_vet, set_treating_vet)

    # -------------------
    # Behavioural methods
    # -------------------

    def issue_resolved(self):
        """Marks the health issue as resolved."""
        self.is_current = False

    def update_treatment_plan(self, treatment_plan):
        """
        Updates the treatment plan with further notes.
        Args: treatment_plan (str): The treatment plan/notes for the health issue, ensuring only a string
             of a minimum length may be passed.
        """
        MIN_LENGTH = 6
        if isinstance(treatment_plan, str) and len(treatment_plan) >= MIN_LENGTH:
            self.__treatment_plan.append(treatment_plan)
        else:
            raise ValueError(f"Invalid treatment plan. Please enter text of at least {MIN_LENGTH} characters.")

    def __str__(self):
        """
        Returns a formatted string containing the health record's details.
        Returns: str: The type, severity, date, description, treatment plan and current status of issue.
        """
        status = 'CURRENT' if self.is_current else 'RESOLVED'
        severity = ['Negligible', 'Minor', 'Moderate', 'Severe'][self.severity_level]
        details = [f"---{self.issue_type.upper()} REPORT---\n"
                   f"This issue is {status}.\n"
                   f"Severity: {severity}\n"
                   f"Date reported: {self.date_reported}\n"
                   f"Description: {self.description}\n"
                   f"Treatment plan/Notes:"]
        for treatment in self.treatment_plan:
            details.append(treatment)
        details.append("")
        return '\n'.join(details)