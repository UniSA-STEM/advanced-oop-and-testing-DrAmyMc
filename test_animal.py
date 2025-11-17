"""
File: test_animal.py
Description: Tests for the abstract Animal parent class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from animal import Animal


class DummyAnimal(Animal):
    """Dummy class required for testing as abstract class cannot be directly instantiated."""

    def make_sound(self):
        return "Dummy sound"

    def eat(self):
        return "Dummy eat"

    def sleep(self):
        return "Dummy sleep"

    def move(self):
        return "Dummy move"


class TestAnimal:
    """Testing suite for the abstract Animal class via DummyAnimal test class."""

    # --- Animal instances for testing ---

    @pytest.fixture
    def animalA(self):
        return DummyAnimal('Paddy', 3, False, 'Lion')

    @pytest.fixture
    def animalB(self):
        return DummyAnimal('Blinky', 1, True, 'Koala')

    # --- Testing direct instantiation of abstract class ---

    def test_abstract_class_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            Animal('Blinky', 1, True, 'Koala')

    # --- Testing getters ---

    def test_get_name(self, animalA, animalB):
        assert animalA.name == 'Paddy'
        assert animalB.name == 'Blinky'

    def test_get_age(self, animalA, animalB):
        assert animalA.age == 3
        assert animalB.age == 1

    def test_get_is_female(self, animalA, animalB):
        assert animalA.is_female is False
        assert animalB.is_female is True

    def test_get_species(self, animalA, animalB):
        assert animalA.species == 'Lion'
        assert animalB.species == 'Koala'

    def test_get_is_native(self, animalA, animalB):
        assert animalA.is_native is False
        assert animalB.is_native is True

    def test_get_dietary_requirements(self, animalA, animalB):
        assert animalA.dietary_requirements == 'meat'
        assert animalB.dietary_requirements == 'leaves'

    def test_get_environment(self, animalA, animalB):
        assert animalA.environment == 'Savannah'
        assert animalB.environment == 'Bushland'

    def test_get_space(self, animalA, animalB):
        assert animalA.space == 200
        assert animalB.space == 20

    def test_get_health_record(self, animalA, animalB):
        assert animalA.health_record == []
        assert animalB.health_record == []

    # --- Testing setters ---

    def test_set_name(self, animalA, animalB):
        """Name setter should accept only str of min 2 char. Invalid input ignored."""
        animalA.name = 'Pa'             # Edge case, 2 char min
        assert animalA.name == 'Pa'     # Valid name change
        animalB.name = 'K'              # Invalid input, only 1 char
        animalB.name = 123              # Invalid input, not a string
        assert animalB.name == 'Blinky' # Original name stands

    def test_set_age(self, animalA, animalB):
        """Age setter should accept only int between 0-200. Invalid input ignored."""
        animalA.age = 0                 # Edge case, 0 min value
        assert animalA.age == 0         # Valid age change
        animalA.age = 200               # Edge case, 200 max value
        assert animalA.age == 200       # Valid name change
        animalB.age = -1                # Invalid input, less than min
        animalB.age = 201               # Invalid input, greater than max
        animalB.age = 'old'             # Invalid input, not an int
        animalB.age = 10.5              # Invalid input, not an int
        assert animalB.age == 1         # Original age stands

    def test_set_is_female(self, animalA, animalB):
        """Is_female setter should accept only bool values. Invalid input ignored."""
        animalA.is_female = True            # Valid bool input
        assert animalA.is_female is True    # Valid sex change
        animalB.is_female = 'no'            # Invalid input, not bool
        assert animalB.is_female is True    # Original sex stands

    def test_set_species(self, animalA, animalB):
        """Species setter should accept only values found in species dictionary (any case). Invalid input ignored."""
        animalA.species = 'Pelican'         # Valid species name
        assert animalA.species == 'Pelican' # Valid species change
        animalA.species = 'tiger'           # Valid species name, lower case accepted
        assert animalA.species == 'Tiger'   # Valid species change, changed to title case
        animalB.species = 'Tigerrr'         # Invalid input, not in species dict
        assert animalB.species == 'Koala'   # Original species stands

    # --- Testing helper methods ---

    def test_lookup_functions(self, animalA):
        animalA.species = 'Fairy Penguin'
        assert animalA.species == 'Fairy Penguin'
        # Values will be automatically updated to Fairy Penguin values due to lookup functions
        assert animalA.is_native is True
        assert animalA.dietary_requirements == 'fish'
        assert animalA.environment == 'Aquatic'
        assert animalA.space == 4

    # --- Testing behavioural methods ---

    def test_make_sound(self, animalA, animalB):
        assert animalA.make_sound() == 'Dummy sound'
        assert animalB.make_sound() == 'Dummy sound'

    def test_eat(self, animalA, animalB):
        assert animalA.eat() == 'Dummy eat'
        assert animalB.eat() == 'Dummy eat'

    def test_sleep(self, animalA, animalB):
        assert animalA.sleep() == 'Dummy sleep'
        assert animalB.sleep() == 'Dummy sleep'

    def test_move(self, animalA, animalB):
        assert animalA.move() == 'Dummy move'
        assert animalB.move() == 'Dummy move'

    def test_string_display(self, animalA):
        s = str(animalA)
        assert 'PADDY' in s
        assert '3' in s
        assert 'Lion' in s
        assert 'Male' in s
        assert 'meat' in s
        assert 'Savannah' in s
        assert 'not native' in s
        assert '200' in s