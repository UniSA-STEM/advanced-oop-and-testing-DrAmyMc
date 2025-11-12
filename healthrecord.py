"""
File: healthrecord.py
Description: Health Record class, to be associated with an animal object.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

class HealthRecord:
    """
    Represents a health record for an animal.
    The Health Record class models a single instance for a single animal, to be attached to that animals
    health history.
    """

    # Four categories for health issues recorded
    ISSUE_TYPE = ['Injury', 'Illness', 'Behavioural', 'Other']

    def __init__(self, issue_type, severity_level, date_reported, description, treatment_plan):
        """
        Initialises a new Health Record instance.

        Args:
            issue_type (str): The category of issue being reported.
            severity_level (int): The severity level from 0-3.
            date_reported (str): The date of the initial report.
            description (str): A description of the health issue
            treatment_plan (str): The initial treatment plan/notes.

        Attributes:
            __issue_type (str): The category of issue being reported.
            __severity_level (int): The severity level from 0-3 (Negligible, Minor, Moderate, Severe).
            __date_reported (str): The date of the initial report.
            __description (str): Description of the health issue.
            __treatment_plan = (list[str]): Treatment plan and notes, including subsequent updates.
        """
        self.issue_type = issue_type                #Utilises the setter for validation of new instances
        self.severity_level = severity_level        #Utilises the setter for validation of new instances
        self.date_reported = date_reported          #Utilises the setter for validation of new instances
        self.description = description              #Utilises the setter for validation of new instances
        self.is_current = True
        self.__treatment_plan = [treatment_plan]

    # --------------
    # Getter methods
    # --------------

    def get_issue_type(self)->str:
        """Returns the health issue type."""
        return self.__issue_type

    def get_severity_level(self)->int:
        """Returns the severity level of the health issue."""
        return self.__severity_level

    def get_date_reported(self)->str:
        """Returns the date that the health issue was reported."""
        return self.__date_reported

    def get_description(self)->str:
        """Returns a description of the health issue."""
        return self.__description

    def get_is_current(self)->bool:
        """Returns whether the health issue is current (True) or resolved (False)."""
        return self.__is_current

    def get_treatment_plan(self)->list:
        """Returns the list of treatment plan notes."""
        return self.__treatment_plan

    # --------------
    # Setter methods
    # --------------

    def set_issue_type(self, issue_type):
        """
        Sets the health issue type.

        Args:
            type (str): The type of health issue being recorded. Must be a valid type.
        """
        if issue_type in HealthRecord.ISSUE_TYPE:
            self.__issue_type = issue_type
        else:
            print(f"Invalid issue type. Please enter one of the following types:\n"
                  f"{HealthRecord.ISSUE_TYPE}")

    def set_severity_level(self, level):
        """
        Updates the severity level, ensuring it remains within a valid range.

        Args:
            severity_level (int): The new severity level (0-3).
        """
        MIN_LEVEL = 0
        MAX_LEVEL = 3
        if isinstance(level, int) and MIN_LEVEL <= level <= MAX_LEVEL:
            self.__severity_level = level
        else:
            print(f"Invalid severity level. Please enter an integer between {MIN_LEVEL} and {MAX_LEVEL}.")

    # This would be better with an imported date file to ensure valid date rather just str.
    def set_date_reported(self, date):
        """
        Updates the date of the report.

        Args:
            date_reported (str): The date that the issue was reported, ensuring only a string of a minimum
            length may be passed.
        """
        MIN_LENGTH = 8
        if isinstance(date, str) and len(date) >= MIN_LENGTH:
            self.__date_reported = date
        else:
            print(f"Invalid date. Please enter text of at least {MIN_LENGTH} characters.")

    def set_description(self, description):
        """
        Updates the description of the health issue.

        Args:
            description (str): Sets the description of the health issue, ensuring only a string of a minimum
            length may be passed.
        """
        MIN_LENGTH = 12
        if isinstance(description, str) and len(description) >= MIN_LENGTH:
            self.__description = description
        else:
            print(f"Invalid description. Please enter text of at least {MIN_LENGTH} characters.")

    def set_is_current(self, is_current):
        """
        Updates the status of the health issue (current = True, resolved = False).

        Args:
            is_current (bool): The status of the health issue.
        """
        if isinstance(is_current, bool):
            self.__is_current = is_current
        else:
            print(f"Invalid current health status. Please enter either True (issue still current) or "
                  f"False (issue resolved).")

    def set_treatment_plan(self, treatment_plan):
        """
        Sets the initial treatment plan/notes.

        Args:
            treatment_plan (str): The treatment plan/notes for the health issue, ensuring only a string
             of a minimum length may be passed.
        """
        MIN_LENGTH = 12
        if isinstance(treatment_plan, str) and len(treatment_plan) >= MIN_LENGTH:
            self.__treatment_plan = [treatment_plan]
        else:
            print(f"Invalid treatment plan. Please enter text of at least {MIN_LENGTH} characters.")

    # --------------------
    # Property definitions
    # --------------------

    issue_type = property(get_issue_type, set_issue_type)
    severity_level = property(get_severity_level, set_severity_level)
    date_reported = property(get_date_reported, set_date_reported)
    description = property(get_description, set_description)
    is_current = property(get_is_current, set_is_current)
    treatment_plan = property(get_treatment_plan, set_treatment_plan)

    # -------------------
    # Behavioural methods
    # -------------------

    def issue_resolved(self):
        """Marks the health issue as resolved."""
        self.is_current = False

    def update_treatment_plan(self, treatment_plan):
        """
        Updates the treatment plan with further notes.

        Args:
            treatment_plan (str): The treatment plan/notes for the health issue, ensuring only a string
             of a minimum length may be passed.
        """
        MIN_LENGTH = 12
        if isinstance(treatment_plan, str) and len(treatment_plan) >= MIN_LENGTH:
            self.__treatment_plan.append(treatment_plan)
        else:
            print(f"Invalid treatment plan. Please enter text of at least {MIN_LENGTH} characters.")

