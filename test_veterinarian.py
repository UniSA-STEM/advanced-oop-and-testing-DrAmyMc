"""
File: test_veterinarian.py
Description: Testing suite for the Veterinarian child class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from veterinarian import Veterinarian


class TestVeterinarian:
    """Testing suite for the Veterinarian class."""

    # --- Veterinarian instances for testing ---

    @pytest.fixture
    def vetA(self):
        return Veterinarian(123456, 'Joe', 'Blogg', '12/11/2025')

    @pytest.fixture
    def vetB(self):
        return Veterinarian(123457, 'Zoe', 'Vlogg', '8/9/2024')

    # --- Testing invalid instantiation ---

    def test_instantiation_with_invalid_arguments(self):
        with pytest.raises(ValueError):
            # Invalid staff id, first name, last name, date hired, and missing argument
            Veterinarian(12345, 'Joe', 'Blogg', '12/11/2025')
            Veterinarian(123456, 'J', 'Blogg', '12/11/2025')
            Veterinarian(123456, 'Joe', 'B', '12/11/2025')
            Veterinarian(123456, 'Joe', 'Blogg', '12/11')
            Veterinarian(123456, 'Joe', 'Blogg')

    # --- Testing getters ---

    def test_get_role(self, vetA, vetB):
        assert vetA.role == 'Veterinarian'
        assert vetB.role == 'Veterinarian'

    def test_get_responsibilities(self, vetA, vetB):
        assert vetA.responsibilities == ['Conduct health checks', 'Treat animals', 'Plan preventive health care']
        assert vetB.responsibilities == ['Conduct health checks', 'Treat animals', 'Plan preventive health care']
