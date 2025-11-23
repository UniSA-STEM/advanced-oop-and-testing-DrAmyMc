"""
File: test_staff.py
Description: Testing suite for the Staff parent class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from staff import Staff
from datetime import date


class DummyEnclosure:
    """Dummy Enclosure class for testing purposes only."""

    def __init__(self, name):
        self.name = name


class TestStaff:
    """Testing suite for the Staff class."""

    # --- Staff instances for testing ---

    @pytest.fixture
    def staffA(self):
        return Staff(123456, 'Joe', 'Blogg', '12/11/2025')

    @pytest.fixture
    def staffB(self):
        return Staff(123457, 'Zoe', 'Vlogg', '8/9/2024')

    # --- Testing invalid instantiation ---

    def test_instantiation_with_missing_argument(self):
        with pytest.raises(TypeError):
            Staff(123451, 'Joe', 'Blogg')

    def test_instantiation_with_invalid_staffid(self):
        with pytest.raises(ValueError):
            Staff(12345, 'Joe', 'Blogg', '12/11/2025')

    def test_instantiation_with_invalid_first_name(self):
        with pytest.raises(ValueError):
            Staff(123458, 'J', 'Blogg', '12/11/2025')

    def test_instantiation_with_invalid_last_name(self):
        with pytest.raises(ValueError):
            Staff(123459, 'Joe', 'B', '12/11/2025')

    def test_instantiation_with_invalid_date_hired(self):
        with pytest.raises(ValueError):
            Staff(123452, 'Joe', 'Blogg', '12/11')

    # --- Testing getters ---

    def test_get_staff_id(self, staffA, staffB):
        assert staffA.staff_id == 123456
        assert staffB.staff_id == 123457

    def test_get_first_name(self, staffA, staffB):
        assert staffA.first_name == 'Joe'
        assert staffB.first_name == 'Zoe'

    def test_get_last_name(self, staffA, staffB):
        assert staffA.last_name == 'Blogg'
        assert staffB.last_name == 'Vlogg'

    def test_get_date_hired(self, staffA, staffB):
        assert staffA.date_hired == date(2025, 11, 12)
        assert staffB.date_hired == date(2024, 9, 8)

    def test_get_role(self, staffA, staffB):
        assert staffA.role == 'Staff'
        assert staffB.role == 'Staff'

    def test_get_responsibilities(self, staffA, staffB):
        assert staffA.responsibilities == []
        assert staffB.responsibilities == []

    def test_get_assigned_enclosures(self, staffA, staffB):
        assert staffA.assigned_enclosures == []
        assert staffB.assigned_enclosures == []

    # --- Testing setters ---

    def test_set_staff_id_valid_min(self, staffA):
        staffA.staff_id = 100000
        assert staffA.staff_id == 100000

    def test_set_staff_id_valid_max(self, staffA):
        staffA.staff_id = 999999
        assert staffA.staff_id == 999999

    def test_set_staff_id_invalid_below_min(self, staffA):
        with pytest.raises(ValueError):
            staffA.staff_id = 99999

    def test_set_staff_id_invalid_above_max(self, staffA):
        with pytest.raises(ValueError):
            staffA.staff_id = 1000000

    def test_set_staff_id_invalid_input_type_float(self, staffA):
        with pytest.raises(ValueError):
            staffA.staff_id = 100100.5

    def test_set_first_name_valid_min_length(self, staffA):
        staffA.first_name = 'Jo'
        assert staffA.first_name == 'Jo'

    def test_set_first_name_invalid_short_string(self, staffA):
        with pytest.raises(ValueError):
            staffA.first_name = 'J'

    def test_set_first_name_invalid_input_type_bool(self, staffA):
        with pytest.raises(ValueError):
            staffA.first_name = False

    def test_set_last_name_valid_min_length(self, staffA):
        staffA.last_name = 'Xi'
        assert staffA.last_name == 'Xi'

    def test_set_last_name_invalid_short_string(self, staffA):
        with pytest.raises(ValueError):
            staffA.last_name = 'X'

    def test_set_last_name_invalid_input_type_bool(self, staffA):
        with pytest.raises(ValueError):
            staffA.last_name = False

    def test_set_date_hired_valid_single_digit(self, staffA):
        staffA.date_hired = '4/5/2023'
        assert staffA.date_hired == date(2023, 5, 4)

    def test_set_date_hired_valid_double_digit(self, staffA):
        staffA.date_hired = '12/10/2026'
        assert staffA.date_hired == date(2026, 10, 12)

    def test_set_date_hired_invalid_input_not_string(self, staffA):
        with pytest.raises(ValueError):
            staffA.date_hired = 4 / 5 / 2023

    def test_set_date_hired_invalid_day(self, staffA):
        with pytest.raises(ValueError):
            staffA.date_hired = '32/12/2025'

    def test_set_date_hired_invalid_month(self, staffA):
        with pytest.raises(ValueError):
            staffA.date_hired = '10/13/2025'

    def test_set_date_hired_invalid_year(self, staffA):
        with pytest.raises(ValueError):
            staffA.date_hired = '12/10/26'

    def test_set_date_hired_invalid_format(self, staffA):
        with pytest.raises(ValueError):
            staffA.date_hired = '4 Nov 2024'

    def test_set_role_valid_min_length(self, staffA):
        staffA.role = 'Shop'
        assert staffA.role == 'Shop'

    def test_set_role_invalid_short_str(self, staffA):
        with pytest.raises(ValueError):
            staffA.role = 'Try'

    def test_set_role_invalid_input_type_bool(self, staffA):
        with pytest.raises(ValueError):
            staffA.role = False

    # --- DummyEnclosure instances for testing helper methods ---

    @pytest.fixture
    def encA(self):
        return DummyEnclosure('Bamboo Forest')

    @pytest.fixture
    def encB(self):
        return DummyEnclosure('African Plains')

    @pytest.fixture
    def encC(self):
        return DummyEnclosure('Bush')

    # --- Testing helper methods ---

    def test_add_assigned_enclosure(self, staffA, encA, encB, encC):
        staffA.add_assigned_enclosure(encA)
        staffA.add_assigned_enclosure(encB)
        staffA.add_assigned_enclosure(encC)
        assert staffA.assigned_enclosures == [encA, encB, encC]

    def test_search_assigned_enclosures_found(self, staffA, encA, encB, encC):
        staffA.add_assigned_enclosure(encA)
        staffA.add_assigned_enclosure(encB)
        staffA.add_assigned_enclosure(encC)
        assert staffA.lookup_assigned_enclosure('African Plains') is encB
        assert staffA.lookup_assigned_enclosure('Bamboo Forest') is encA

    def test_search_assigned_enclosures_not_found(self, staffA, encA, encB, encC):
        staffA.add_assigned_enclosure(encA)
        staffA.add_assigned_enclosure(encB)
        staffA.add_assigned_enclosure(encC)
        assert staffA.lookup_assigned_enclosure('Africa') is None

    # --- Testing string display ---

    def test_string_display(self, staffA):
        s = str(staffA)
        assert 'STAFF' in s
        assert 'Joe Blogg' in s
        assert '123456' in s
        assert '2025-11-12' in s
        assert 'Responsibilities' not in s
        assert 'Assigned Enclosures' not in s

    def test_string_display_alt_values(self, staffB, encA, encB, encC):
        staffB.role = 'Security'
        staffB.add_assigned_enclosure(encA)
        staffB.add_assigned_enclosure(encB)
        staffB.add_assigned_enclosure(encC)
        s = str(staffB)
        assert 'SECURITY' in s
        assert 'Zoe Vlogg' in s
        assert '123457' in s
        assert '2024-09-08' in s
        assert 'Assigned Enclosures' in s
        assert 'Bamboo Forest' in s
        assert 'African Plains' in s
        assert 'Bush' in s
