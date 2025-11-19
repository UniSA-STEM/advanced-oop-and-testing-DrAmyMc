"""
File: test_zoo.py
Description: Testing suite for the Zoo class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from zoo import Zoo


class TestZoo:
    """Testing suite for the Zoo class."""

    # --- Zoo instances for testing ---

    @pytest.fixture
    def zooA(self):
        return Zoo('Halls Gap Zoo')

    @pytest.fixture
    def zooB(self):
        return Zoo('Grampians Zoo')

    # --- Testing invalid instantiation ---

    def test_instantiation_with_invalid_arguments(self):
        with pytest.raises(ValueError):
            # Invalid name, and missing argument
            Zoo('X')
            Zoo()

    # --- Testing getters ---

    def test_get_name(self, zooA, zooB):
        assert zooA.name == 'Halls Gap Zoo'
        assert zooB.name == 'Grampians Zoo'

    def test_get_animals(self, zooA, zooB):
        assert zooA.animals == []
        assert zooB.animals == []

    def test_get_enclosures(self, zooA, zooB):
        assert zooA.enclosures == []
        assert zooB.enclosures == []

    def test_get_staff(self, zooA, zooB):
        assert zooA.staff == []
        assert zooB.staff == []

    # --- Testing setters ---

    def test_set_name(self, zooA, zooB):
        zooA.name = 'Zoo'
        assert zooA.name == 'Zoo'
        zooB.name = 'Australian Zoo'
        assert zooB.name == 'Australian Zoo'
        with pytest.raises(ValueError):
            zooA.name = 'Zo'
            zooB.name = 1
            zooA.name = False
