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
from enclosure import Enclosure


class TestZookeeper:
    """Testing suite for the Zookeeper class."""

    # --- Enclosure instances for testing helper methods ---

    @pytest.fixture
    def encA(self):
        return Enclosure('African Plains', 'Savannah', 2000)

    @pytest.fixture
    def encB(self):
        enc = Enclosure('Penguin Palace', 'Aquatic', 50)
        enc.cleanliness_level = 3
        enc.animal_type = 'Fairy Penguin'
        return enc

    # --- Zookeeper instance for testing ---

    @pytest.fixture
    def keeperA(self, encA, encB):
        keeper = Zookeeper(123456, 'Joe', 'Blogg', '12/11/2025')
        keeper.add_assigned_enclosure(encA)
        keeper.add_assigned_enclosure(encB)
        return keeper

    # --- Testing getters ---

    def test_get_role(self, keeperA):
        assert keeperA.role == 'Zookeeper'

    def test_get_responsibilities(self, keeperA):
        assert keeperA.responsibilities == ['Feed animals', 'Clean enclosures', 'Exhibit planning']

    def test_get_assigned_enclosures(self, keeperA):
        assert len(keeperA.assigned_enclosures) == 2

    # --- Testing behavioural methods ---

    def test_clean_enclosure_not_assigned(self, keeperA):
        msg = keeperA.clean_enclosure('Penguins')
        assert msg  == 'Cannot clean Penguins. Not assigned to this enclosure.'

    def test_clean_enclosure_not_dirty(self, keeperA):
        msg = keeperA.clean_enclosure('African Plains')
        assert msg == 'Cannot clean African Plains. This enclosure is already pristine.'

    def test_clean_enclosure_successful_clean(self, keeperA, encB):
        msg = keeperA.clean_enclosure('Penguin Palace')
        assert encB.cleanliness_level == 5
        assert msg == 'Joe Blogg cleaned the Penguin Palace enclosure.'

    def test_feed_animals_enclosure_not_assigned(self, keeperA):
        msg = keeperA.feed_animals('Penguins')
        assert msg == 'Cannot feed animals in Penguins. Not assigned to this enclosure.'

    def test_feed_animals_empty_enclosure(self, keeperA):
        msg = keeperA.feed_animals('African Plains')
        assert msg == 'Cannot feed animals in African Plains. This enclosure is empty.'

    def test_feed_animals_successful_feed(self, keeperA):
        msg = keeperA.feed_animals('Penguin Palace')
        assert msg == 'Joe Blogg fed fish to the Fairy Penguins in Penguin Palace.'

    # --- Testing string display ---

    def test_string_display(self, keeperA):
        s = str(keeperA)
        assert 'ZOOKEEPER' in s
        assert 'Responsibilities' in s
        assert 'Feed animals' in s
        assert 'Clean enclosures' in s
        assert 'Exhibit planning' in s
        assert 'Assigned Enclosures' in s