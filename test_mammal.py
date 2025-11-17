'''
File: test_animal.py
Description: A brief description of this Python module.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest

from animal import Animal
from animal import Mammal
from animal import Bird
from animal import Reptile


class TestMammal:
    """
    Direct tests for the Animal superclass and subclasses for animal creation, setting attributes
    and string display.

    Tests:
        - Creation of animal instances (valid and invalid cases).
        - Setting attributes manually (valid and invalid cases).
        - Displaying string representations.
    """

    @pytest.fixture
    def mammal(self):
        return Mammal("Paddy", 3, False, "Lion", "Shaggy")

    @pytest.fixture
    def bird(self):
        return Bird("Percival", 2, True, "Pelican", 2.1, False)

    @pytest.fixture
    def reptile(self):
        return Reptile("Lizzie", 1, False, "Lace Monitor", 18, False)

    def test_get_name(self, mammal):
        assert mammal.name == 'Paddy'

    assert mammal.age == 3
    assert mammal.is_female == False
    assert mammal.species == 'Lion'
    assert mammal.is_native == False
    assert mammal.dietary_requirements == 'meat'
    assert mammal.environemnt == 'Savannah'
    assert mammal.space == 200
    assert mammal.health_record == []
    assert mammal.fur_type == 'Shaggy'

    # --- Attempt to create animals with invalid species ---
    cat2 = Mammal("Paddy", 3, False, "llion", "Shaggy")
    print(cat2)

    # --- Modify animal attributes to valid values ---
    cat.name = "Puddy"
    cat.age = 0
    cat.species = "tiger"  # Will automatically convert to title case when matching
    cat.is_female = True
    cat.is_pregnant = True
    print(cat)

    # --- Attempt to modify animal attributes to invalid values ---
    cat.name = "P"
    cat.age = -1
    cat.age = 201
    cat.age = "old"
    cat.species = "llion"
    cat.is_female = 'female'
    cat.is_pregnant = 'yes'
    print(cat)


class TestMammal:
    """
    Direct tests for the Animal superclass and subclasses for animal creation, setting attributes
    and string display.

    Tests:
        - Creation of animal instances (valid and invalid cases).
        - Setting attributes manually (valid and invalid cases).
        - Displaying string representations.
    """

    @pytest.fixture
    def mammal(self):
        return Mammal("Paddy", 3, False, "Lion", "Shaggy")

    def test_get_name(self, mammal):
        assert mammal.name == 'Paddy'

    def test_get_age(self, mammal):
        assert mammal.age == 3

    def test_get_is_female(self, mammal):
        assert mammal.is_female == False

    def test_get_species(self, mammal):
        assert mammal.species == 'Lion'

    def test_get_is_native(self, mammal):
        assert mammal.is_native == False

    def test_get_dietary_requirements(self, mammal):
        assert mammal.dietary_requirements == 'meat'

    def test_get_environment(self, mammal):
        assert mammal.environemnt == 'Savannah'

    def test_get_space(self, mammal):
        assert mammal.space == 200

    def test_get_health_record(self, mammal):
        assert mammal.health_record == []

    def test_get_fur_type(self, mammal):
        assert mammal.fur_type == 'Shaggy'

    def test_get_is_pregnant(self, mammal):
        assert mammal.is_pregnant == False

    # --- Attempt to create animals with invalid species ---
    cat2 = Mammal("Paddy", 3, False, "llion", "Shaggy")
    print(cat2)

    # --- Modify animal attributes to valid values ---
    cat.name = "Puddy"
    cat.age = 0
    cat.species = "tiger"  # Will automatically convert to title case when matching
    cat.is_female = True
    cat.is_pregnant = True
    print(cat)

    # --- Attempt to modify animal attributes to invalid values ---
    cat.name = "P"
    cat.age = -1
    cat.age = 201
    cat.age = "old"
    cat.species = "llion"
    cat.is_female = 'female'
    cat.is_pregnant = 'yes'
    print(cat)
