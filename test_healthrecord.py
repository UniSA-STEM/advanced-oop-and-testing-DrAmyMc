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


# For testing purposes
class DummyVet:
    def __init__(self, name):
        self.name = name


class TestHealthRecord:
    """Testing suite for the HealthRecord class."""

    # --- Vet and HealthRecord instances for testing ---

    @pytest.fixture
    def vetA(self):
        return DummyVet('Dr Bob')

    @pytest.fixture
    def recA(self, vetA):
        return HealthRecord(0, 2, '12/11/2025','Laceration',
                            'Clean and bandage.', vetA)

    @pytest.fixture
    def recB(self, vetA):
        return HealthRecord(2, 1, '8/9/2024','Lethargy',
                            'Monitor for fever.', vetA)

    # --- Testing invalid instantiation ---

    def test_instantiation_with_missing_argument(self):
        with pytest.raises(TypeError):
            HealthRecord(0, 2, '12/11/2025', 'Laceration',
                         'Clean and bandage.')

    def test_instantiation_with_invalid_issue_type(self, vetA):
        with pytest.raises(ValueError):
            HealthRecord(3, 2, '12/11/2025', 'Laceration',
                         'Clean and bandage.', vetA)

    def test_instantiation_with_invalid_severity_type(self, vetA):
        with pytest.raises(ValueError):
            HealthRecord(0, 4, '12/11/2025', 'Laceration',
                         'Clean and bandage.', vetA)

    def test_instantiation_with_invalid_date_reported(self, vetA):
        with pytest.raises(ValueError):
            HealthRecord(0, 2, '12 Nov 2025', 'Laceration',
                         'Clean and bandage.', vetA)

    def test_instantiation_with_invalid_description(self, vetA):
        with pytest.raises(ValueError):
            HealthRecord(0, 2, '12/11/2025', 'Lac',
                         'Clean and bandage.', vetA)

    def test_instantiation_with_invalid_initial_plan(self, vetA):
        with pytest.raises(ValueError):
            HealthRecord(0, 2, '12/11/2025', 'Laceration',
                         'Clean', vetA)

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
        assert recA.description == 'Laceration'
        assert recB.description == 'Lethargy'

    def test_get_treatment_plan(self, recA, recB):
        assert recA.treatment_plan == ['Clean and bandage.']
        assert recB.treatment_plan == ['Monitor for fever.']

    def test_get_is_current(self, recA, recB):
        assert recA.is_current is True
        assert recB.is_current is True

    def test_get_vet(self, recA, recB, vetA):
        assert recA.vet is vetA
        assert recB.vet is vetA

    # --- Testing setters ---

    def test_set_issue_type_valid(self, recA):
        recA.issue_type = 1
        assert recA.issue_type == 'Illness'
        recA.issue_type = 2
        assert recA.issue_type == 'Behavioural Issue'
        recA.issue_type = 0
        assert recA.issue_type == 'Injury'

    def test_set_issue_type_invalid_below_min(self, recA):
        with pytest.raises(ValueError):
            recA.issue_type = -1

    def test_set_issue_type_invalid_above_max(self, recA):
        with pytest.raises(ValueError):
            recA.issue_type = 3

    def test_set_issue_type_invalid_input_float(self, recA):
        with pytest.raises(ValueError):
            recA.issue_type = 1.5

    def test_set_issue_type_invalid_input_bool(self, recA):
        with pytest.raises(ValueError):
            recA.issue_type = False

    def test_set_severity_level_valid_min(self, recA):
        recA.severity_level = 0
        assert recA.severity_level == 0

    def test_set_severity_level_valid_max(self, recA):
        recA.severity_level = 3
        assert recA.severity_level == 3

    def test_set_severity_level_invalid_below_min(self, recA):
        with pytest.raises(ValueError):
            recA.severity_level = -1

    def test_set_severity_level_invalid_above_max(self, recA):
        with pytest.raises(ValueError):
            recA.severity_level = 4

    def test_set_severity_level_invalid_input_float(self, recA):
        with pytest.raises(ValueError):
            recA.severity_level = 1.5

    def test_set_severity_level_invalid_input_bool(self, recA):
        with pytest.raises(ValueError):
            recA.severity_level = False

    def test_set_date_reported_valid(self, recA):
        recA.date_reported = '4/5/2023'
        assert recA.date_reported == date(2023, 5, 4)
        recA.date_reported = '12/10/2026'
        assert recA.date_reported == date(2026, 10, 12)

    def test_set_date_reported_invalid_not_string(self, recA):
        with pytest.raises(ValueError):
            recA.date_reported = 4/5/2023

    def test_set_date_reported_invalid_day(self, recA):
        with pytest.raises(ValueError):
            recA.date_reported = '32/13/2025'

    def test_set_date_reported_invalid_month(self, recA):
        with pytest.raises(ValueError):
            recA.date_reported = '10/13/2025'

    def test_set_date_reported_invalid_year(self, recA):
        with pytest.raises(ValueError):
            recA.date_reported = '12/10/26'

    def test_set_date_reported_invalid_format(self, recA):
        with pytest.raises(ValueError):
            recA.date_reported = '4 Nov 2024'

    def test_set_description_valid(self, recA):
        recA.description = 'Unwell'
        assert recA.description == 'Unwell'

    def test_set_description_invalid_short_str(self, recA):
        with pytest.raises(ValueError):
            recA.description = 'Limpy'

    def test_set_description_invalid_input_bool(self, recA):
        with pytest.raises(ValueError):
            recA.description = True

    def test_set_treatment_plan_valid(self, recA):
        recA.treatment_plan = 'Unwell'
        assert recA.treatment_plan == ['Unwell']

    def test_set_treatment_plan_invalid_short_str(self, recA):
        with pytest.raises(ValueError):
            recA.treatment_plan = 'Limpy'

    def test_set_treatment_plan_invalid_input_bool(self, recA):
        with pytest.raises(ValueError):
            recA.treatment_plan = True

    def test_set_is_current_valid(self, recA):
        recA.is_current = False
        assert recA.is_current is False
        recA.is_current = True
        assert recA.is_current is True

    def test_set_is_current_invalid_input_int(self, recA):
        with pytest.raises(ValueError):
            recA.is_current = 1


# # def test_update_health_record():
# #
# #     # --- Create and display valid health record ---
# #     record = HealthRecord("Injury", 3, "12 Nov 2025",
# #                           "Laceration on left front leg", "Clean and bandage wound and monitor.")
# #     print(record)
# #
# #     # --- Add treatment plan notes then resolve issue ---
# #     record.update_treatment_plan("Change dressing twice daily.")            #Valid
# #     record.update_treatment_plan("Continue to monitor for two more days.")  #Valid
# #     record.update_treatment_plan("Ok")                                      #Invalid output, length insufficient
# #     record.issue_resolved()
# #     print(record)
# #
# # def test_add_health_record():#
# #     # --- Create animal ---
# #     cat = Mammal("Paddy", 3, "Lion", False)
# #     print(cat)
# #
# #     # --- Create and display valid health record ---
# #     cat.add_health_record("Injury", 3, "12 Nov 2025",
# #                           "Laceration on left front leg", "Clean and bandage wound and monitor.")
