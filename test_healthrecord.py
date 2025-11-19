"""
File: test_healthrecord.py
Description: Testing suite for the HealthRecord class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from healthrecord import HealthRecord
from datetime import date


class TestHealthRecord:
    """Testing suite for the HealthRecord class."""

    # --- HealthRecord instances for testing ---

    @pytest.fixture
    def recA(self):
        return HealthRecord('Injury', 2, '12/11/2025','Laceration on '
                            'left front leg', 'Clean and bandage wound and monitor.')

    @pytest.fixture
    def recB(self):
        return HealthRecord('Behavioural Issue', 1, '8/9/2024',
                            'Lethargy', 'Monitor for signs of fever.')

    # --- Testing invalid instantiation ---

    # def test_instantiation_with_invalid_arguments(self):
    #     with pytest.raises(ValueError):
    #         # Invalid name, type, size, and missing argument
    #         Enclosure('R', 'Terrarium', 20)
    #         Enclosure('Reptile House', 'Terrrrarium', 20)
    #         Enclosure('Reptile House', 'Terrarium', 0)
    #         Enclosure('Reptile House', 'Terrarium')

    # --- Testing getters ---

    def test_get_issue_type(self, recA, recB):
        assert recA.issue_type == 'Injury'
        assert recB.issue_type == 'Behavioural Issue'

    def test_get_severity_level(self, recA, recB):
        assert recA.severity_level == 2
        assert recB.severity_level == 1

    def test_get_date_reported(self, recA, recB):
        assert recA.date_reported == date(2025, 11, 12)
        assert recB.date_reported == date(2024, 9, 8)

    def test_get_description(self, recA, recB):
        assert recA.description == 'Laceration on left front leg'
        assert recB.description == 'Lethargy'

    def test_get_treatment_plan(self, recA, recB):
        assert recA.treatment_plan == ['Clean and bandage wound and monitor.']
        assert recB.treatment_plan == ['Monitor for signs of fever.']

    def test_is_current(self, recA, recB):
        assert recA.is_current is True
        assert recB.is_current is True

    # --- Testing setters ---

    def test_set_issue_type(self, recA, recB):
        """Issue type setter should only accept issues from defined list."""
        recA.issue_type = 'Behavioural Issue'
        assert recA.issue_type == 'Behavioural Issue'
        recB.issue_type = 'Illness'
        assert recB.issue_type == 'Illness'
        with pytest.raises(ValueError):
            recA.issue_type = 'Injure'
            recB.issue_type = 1
            recB.issue_type = False

    def test_set_severity_level(self, recA, recB):
        """Severity level setter should only accept integers from 0-3."""
        recA.severity_level = 3
        assert recA.severity_level == 3
        recB.severity_level = 0
        assert recB.severity_level == 0
        with pytest.raises(ValueError):
            recA.severity_level = 4
            recA.severity_level = -1
            recB.severity_level = 2.5
            recB.severity_level = 'bad'

    def test_date_reported(self, recA, recB):
        """Date reported setter should only accept dates in string format dd/mm/yyyy."""
        recA.date_reported = '4/5/2023'
        assert recA.date_reported == date(2023, 5, 4)
        recB.date_reported = '12/10/2026'
        assert recB.date_reported == date(2026, 10, 12)
        with pytest.raises(ValueError):
            recA.date_reported = 4/5/2023
            recA.date_reported = '10/13/2025'
            recA.date_reported = '12/10/26'
            recB.date_reported = '4 Nov 2024'
            recB.date_reported = 123

    def test_description(self, recA, recB):
        pass

    # def test_set_name(self, encA, encB):
    #     """Name setter should only accept a string of min length 3 char."""
    #     encA.name = 'Wow'  # Edge case, 3 char min
    #     assert encA.name == 'Wow'  # Valid name change
    #     encB.name = 'Lap'  # Edge case, 3 char min
    #     assert encB.name == 'Lap'  # Valid name change
    #     with pytest.raises(ValueError):
    #         encA.name = ''  # Invalid input, empty string
    #         encA.name = 'La'  # Invalid input, below min char
    #         encB.name = 123  # Invalid input, not a string

# def test_create_health_record():
#
#     # --- Create and display valid health record ---
#     record = HealthRecord("Injury", 3, "12 Nov 2025",
#                           "Laceration on left front leg", "Clean and bandage wound and monitor.")
#     print(record)
#
#     # --- Attempt to create health record with invalid type ---
#     record2 = HealthRecord("Leg", 3, "12 Nov 2025",
#                           "Laceration on left front leg", "Clean and bandage wound and monitor.")
#     print(record2)
#
#     # --- Modify health record attributes to valid values ---
#     record.issue_type = 'Illness'
#     record.severity_level = 0
#     record.date_reported = "10 Nov 2025"
#     record.description = "Lethargic due to minor fever"
#     record.is_current = False
#     record.treatment_plan = "Monitor, but no other changes necessary."
#     print(record)
#
#     # --- Attempt to modify health record attributes to invalid values ---
#     record.issue_type = 'Leg'
#     record.severity_level = -1
#     record.severity_level = 4
#     record.severity_level = "bad"
#     record.date_reported = "10th"
#     record.description = "Bad"
#     record.is_current = "yes"
#     record.treatment_plan = "None"
#     print(record)
#
# def test_update_health_record():
#     """
#     Direct tests for the HealthRecord class for updating health records.
#
#     Tests:
#         - Updating health record (valid and invalid cases).
#         - Displaying string representations.
#     """
#     print("\n=== TEST: Updating of Health Record ===\n")
#
#     # --- Create and display valid health record ---
#     record = HealthRecord("Injury", 3, "12 Nov 2025",
#                           "Laceration on left front leg", "Clean and bandage wound and monitor.")
#     print(record)
#
#     # --- Add treatment plan notes then resolve issue ---
#     record.update_treatment_plan("Change dressing twice daily.")            #Valid
#     record.update_treatment_plan("Continue to monitor for two more days.")  #Valid
#     record.update_treatment_plan("Ok")                                      #Invalid output, length insufficient
#     record.issue_resolved()
#     print(record)
#
# def test_add_health_record():
#     """
#     Tests creation of health records for an animal.
#
#     Tests:
#         - Creation of a Health Record instance for a specific animal.
#     """
#     print("\n=== TEST: Add Health Record to Animal ===\n")
#
#     # --- Create animal ---
#     cat = Mammal("Paddy", 3, "Lion", False)
#     print(cat)
#
#     # --- Create and display valid health record ---
#     cat.add_health_record("Injury", 3, "12 Nov 2025",
#                           "Laceration on left front leg", "Clean and bandage wound and monitor.")
