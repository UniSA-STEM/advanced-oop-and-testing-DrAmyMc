"""
File: healthrecord.py
Description: Health Record class, to be associated with an animal object.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

class HealthRecord:
    ISSUE_TYPE = ['Injury', 'Illness', 'Behavioural', 'Other']

    def __init__(self, issue_type, severity_level, date_reported, description, treatment_plan):
        self.issue_type = issue_type
        self.__severity_level = severity_level
        self.__date_reported = date_reported
        self.__description = description
        self.__is_current = True
        self.__treatment_plan = [treatment_plan]

    # --------------
    # Getter methods
    # --------------

    def get_issue_type(self)->str:
        return self.__issue_type

    def get_severity_level(self)->int:
        return self.__severity_level

    def get_date_reported(self)->str:
        return self.__date_reported

    def get_description(self)->str:
        return self.__description

    def get_is_current(self)->bool:
        return self.__is_current

    def get_treatment_plan(self)->list:
        return self.__treatment_plan

    # --------------
    # Setter methods
    # --------------

    def set_issue_type(self, issue_type):
        if issue_type in HealthRecord.ISSUE_TYPE:
            self.__issue_type = issue_type
        else:
            print(f"Please enter a valid issue type from the following list:\n"
                  f"{HealthRecord.ISSUE_TYPE}")

    def set_severity_level(self, level):
        MIN_LEVEL = 0
        MAX_LEVEL = 3
        if isinstance(level, int) and MIN_LEVEL <= level <= MAX_LEVEL:
            self.__severity_level = level
        else:
            print(f"Please enter")

    def set_date_reported(self, date):
        pass

    def set_description(self, description):
        pass

    def set_is_current(self, is_current):
        pass

    def set_treatment_plan(self, treatment_plan):
        pass

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



