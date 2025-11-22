"""
File: veterinarian.py
Description: Veterinarian child class from Staff parent class, for use in a Zoo.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Staff
from healthrecord import HealthRecord


class Veterinarian(Staff):
    """A veterinarian with responsibilities and behaviours unique to the veterinarian role, extending Staff."""

    def __init__(self, staff_id, first_name, last_name, year_hired):
        """
        Initialises a new Veterinarian instance of the Veterinarian subclass.

        Notes:
            Attributes such as staff_id, first_name, last_name, and date_hired are initialised by the parent class.
        """
        super().__init__(staff_id, first_name, last_name, year_hired)
        self._responsibilities = ['Conduct health checks', 'Treat animals', 'Plan preventative health care']

    # -------------------
    # Behavioural methods
    # -------------------

    def conduct_health_checks(self, enclosure_name):
        """Checks the health status of the animals in an assigned enclosure."""
        enclosure = self.lookup_assigned_enclosure(enclosure_name)
        # Will not conduct health checks if not assigned
        if enclosure is None:
            return f"Cannot conduct health checks in {enclosure_name}. Not assigned to this enclosure."
        # Will not conduct health checks if enclosure is empty
        elif enclosure.animal_type is None:
            return f"Cannot conduct health checks in {enclosure_name}. This enclosure is empty."
        # Conducts health checks if assigned to enclosure and animals present.
        else:
            return (f"{self.first_name} {self.last_name} conducted health checks on the {enclosure.animal_type}s "
                    f"in {enclosure.name}.")

    def create_health_record(self, animal, issue_type, severity_level, date_reported, description, treatment_plan)->HealthRecord:
        """
        Initialises a new Health Record instance for the animal.

        Args:
            issue_type (str): The category of issue being reported.
            severity_level (int): The severity level from 0-3.
            date_reported (str): The date of the initial report.
            description (str): A description of the health issue
            treatment_plan (str): The initial treatment plan/notes.
        """
        record = HealthRecord(issue_type, severity_level, date_reported, description, treatment_plan, self)
        animal.add_health_record(record)
        animal.on_display = False
        return record

    def add_treatment_note(self, animal, treatment_note):
        """Adds a treatment note for an existing health condition."""
        record = animal.lookup_current_record()
        if record is None:
            raise ValueError(f"{animal.name} the {animal.species} does not have a current health record to update.")
        record.update_treatment_plan(treatment_note)

    def mark_issue_resolved(self, animal):
        """Marks an existing health conditions as resolved."""
        record = animal.lookup_current_record()
        if record is None:
            raise ValueError(f"{animal.name} the {animal.species} does not have a current health record to resolve.")
        record.mark_issue_resolved()
        animal.on_display = True