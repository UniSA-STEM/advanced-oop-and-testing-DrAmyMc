"""
File: test_healthrecord.py
Description: Testing suite for the HealthRecord class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""
from random import betavariate
from tabnanny import verbose

import pytest
from healthrecord import HealthRecord
from datetime import date


# For testing purposes
class DummyVet:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class TestHealthRecord:
    """Testing suite for the HealthRecord class."""

    # --- Vet instances for testing ---

    @pytest.fixture
    def vetA(self):
        return DummyVet('Bob', 'Fobb')

    @pytest.fixture
    def vetB(self):
        return DummyVet('Zoe', 'Pesco')

    # --- HealthRecord instances for testing ---

    @pytest.fixture
    def recA(self, vetA):
        return HealthRecord(0, 2, '12/11/2025','Laceration',
                            'Clean and bandage.', vetA)

    @pytest.fixture
    def recB(self, vetB):
        return HealthRecord(2, 1, '8/9/2024','Lethargy',
                            'Monitor for fever.', vetB)

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

    def test_get_vet(self, recA, recB, vetA, vetB):
        assert recA.vet is vetA
        assert recB.vet is vetB

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

    def test_set_vet_valid(self, recA, recB, vetA, vetB):
        recA.vet = vetB
        assert recA.vet is vetB
        recB.vet = vetA
        assert recB.vet is vetA

    # --- Testing helper methods ---

    def test_mark_issue_resolved_valid(self, recA, recB):
        recA.mark_issue_resolved()
        assert recA.is_current is False
        recB.mark_issue_resolved()
        assert recB.is_current is False
        recB.mark_issue_resolved()
        assert recB.is_current is False

    def test_update_health_record_valid_min_length(self, recA):
        recA.update_treatment_plan('Test')
        assert recA.treatment_plan == ['Clean and bandage.', 'Test']

    def test_update_health_record_valid_multiple_updates(self, recA):
        recA.update_treatment_plan('Test')
        recA.update_treatment_plan('Check')
        recA.update_treatment_plan('Monitor')
        assert len(recA.treatment_plan) == 4

    def test_update_health_record_invalid_short_string(self, recA):
        with pytest.raises(ValueError):
            recA.update_treatment_plan('Meh')

    def test_update_health_record_invalid_input_type_int(self, recA):
        with pytest.raises(ValueError):
            recA.update_treatment_plan(1234)

    # --- Testing string display ---

    @pytest.fixture
    def vetA(self):
        return DummyVet('Bob', 'Fobb')
    @pytest.fixture
    def vetB(self):
        return DummyVet('Zoe', 'Pesco')
    @pytest.fixture
    def recA(self, vetA):
        return HealthRecord(0, 2, '12/11/2025','Laceration',
                            'Clean and bandage.', vetA)
    @pytest.fixture
    def recB(self, vetB):
        return HealthRecord(2, 1, '8/9/2024','Lethargy',
                            'Monitor for fever.', vetB)
    def test_string_display(self, recA):
        s = str(recA)
        assert 'INJURY REPORT' in s
        assert 'CURRENT' in s
        assert 'Moderate' in s
        assert '2025-11-12' in s
        assert 'Dr Bob Fobb' in s
        assert 'Laceration' in s
        assert 'Clean and bandage.' in s

    def test_string_display_alt_values(self, recB):
        recB.update_treatment_plan('Mild fever only.')
        recB.update_treatment_plan('No fever.')
        recB.mark_issue_resolved()
        s = str(recB)
        assert 'BEHAVIOURAL ISSUE REPORT' in s
        assert 'RESOLVED' in s
        assert 'Minor' in s
        assert '2024-09-08' in s
        assert 'Dr Zoe Pesco' in s
        assert 'Lethargy' in s
        assert 'Monitor for fever.' in s
        assert 'Mild fever only.' in s
        assert 'No fever.' in s