"""
File: test_zookeeper.py
Description: Testing suite for the Zookeeper child class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from zookeeper import Zookeeper


class TestZookeeper:
    """Testing suite for the Zookeeper class."""

    # --- Zookeeper instances for testing ---

    @pytest.fixture
    def keeperA(self):
        return Zookeeper(123456, 'Joe', 'Blogg', '12/11/2025')

    @pytest.fixture
    def keeperB(self):
        return Zookeeper(123457, 'Zoe', 'Vlogg', '8/9/2024')

    # --- Testing invalid instantiation ---

    def test_instantiation_with_invalid_arguments(self):
        with pytest.raises(ValueError):
            # Invalid staff id, first name, last name, date hired, and missing argument
            Zookeeper(12345, 'Joe', 'Blogg', '12/11/2025')
            Zookeeper(123456, 'J', 'Blogg', '12/11/2025')
            Zookeeper(123456, 'Joe', 'B', '12/11/2025')
            Zookeeper(123456, 'Joe', 'Blogg', '12/11')
            Zookeeper(123456, 'Joe', 'Blogg')

    # --- Testing getters ---

    def test_get_role(self, keeperA, keeperB):
        assert keeperA.role == 'Zookeeper'
        assert keeperB.role == 'Zookeeper'

    def test_get_responsibilities(self, keeperA, keeperB):
        assert keeperA.responsibilities == ['Feed animals', 'Clean enclosures', 'Exhibit planning']
        assert keeperB.responsibilities == ['Feed animals', 'Clean enclosures', 'Exhibit planning']

