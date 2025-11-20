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

    def test_instantiation_with_invalid_arguments(self):
        with pytest.raises(ValueError):
            # Invalid staff id, first name, last name, date hired, and missing argument
            Staff(12345, 'Joe', 'Blogg', '12/11/2025')
            Staff(123458, 'J', 'Blogg', '12/11/2025')
            Staff(123459, 'Joe', 'B', '12/11/2025')
            Staff(123452, 'Joe', 'Blogg', '12/11')
            Staff(123451, 'Joe', 'Blogg')

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

    def test_set_staff_id(self, staffA, staffB):
        """Staff ID setter must be a 6 digit integer, from 100000 to 999999."""
        staffA.staff_id = 100000
        assert staffA.staff_id == 100000
        staffB.staff_id = 999999
        assert staffB.staff_id == 999999
        with pytest.raises(ValueError):
            staffA.staff_id = 99999
            staffA.staff_id = 1000000
            staffB.staff_id = -111111
            staffB.staff_id = 100100.5
            staffB.staff_id = 'VIP'
            staffB.staff_id = False

    def test_set_first_name(self, staffA, staffB):
        """Setter for first name requires a str of min length 2 char."""
        staffA.first_name = 'Jo'
        assert staffA.first_name == 'Jo'
        staffB.first_name = 'Xi'
        assert staffB.first_name == 'Xi'
        with pytest.raises(ValueError):
            staffA.first_name = 'J'
            staffB.first_name = 1
            staffB.first_name = False

    def test_set_last_name(self, staffA, staffB):
        """Setter for last name requires a str of min length 2 char."""
        staffA.last_name = 'Bo'
        assert staffA.last_name == 'Bo'
        staffB.last_name = 'Li'
        assert staffB.last_name == 'Li'
        with pytest.raises(ValueError):
            staffA.last_name = 'X'
            staffB.last_name = 1
            staffB.last_name = False

    def test_set_date_hired(self, staffA, staffB):
        """Date hired setter should only accept dates in string format dd/mm/yyyy."""
        staffA.date_hired = '4/5/2023'
        assert staffA.date_hired == date(2023, 5, 4)
        staffB.date_hired = '12/10/2026'
        assert staffB.date_hired == date(2026, 10, 12)
        with pytest.raises(ValueError):
            staffA.date_hired = 4/5/2023
            staffA.date_hired = '10/13/2025'
            staffA.date_hired = '12/10/26'
            staffB.date_hired = '4 Nov 2024'
            staffB.date_hired = 123

    def test_set_role(self, staffA, staffB):
        """Role setter should only accept string of 4 char min."""
        staffA.role = 'Security'
        assert staffA.role == 'Security'
        staffB.role = 'Food'
        assert staffB.role == 'Food'
        with pytest.raises(ValueError):
            staffA.role = 'Try'
            staffB.role = 1
            staffB.role = False
