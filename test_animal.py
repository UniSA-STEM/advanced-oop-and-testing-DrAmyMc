'''
File: test_animal.py
Description: Tests for the abstract Animal parent class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest

from animal import Animal


# Required as abstract class cannot be instantiated
class DummyAnimal(Animal):

    def make_sound(self):
        return "Dummy sound"

    def eat(self):
        return "Dummy eat"

    def sleep(self):
        return "Dummy sleep"

    def move(self):
        return "Dummy move"


class TestAnimal:
    """
    Direct tests for the Animal superclass and subclasses for animal creation, setting attributes
    and string display.

    Tests:
        - Creation of animal instances (valid and invalid cases).
        - Setting attributes manually (valid and invalid cases).
        - Displaying string representations.
    """
    @pytest.fixture
    def animalA(self):
        return DummyAnimal('Paddy', 3, False, 'Lion')

    @pytest.fixture
    def animalB(self):
        return DummyAnimal('Blinky', 1, True, 'Koala')

    def test_get_name(self, animalA, animalB):
        assert animalA.name == 'Paddy'
        assert animalB.name == 'Blinky'

    def test_get_age(self, animalA, animalB):
        assert animalA.age == 3
        assert animalB.age == 1

    def test_get_is_female(self, animalA, animalB):
        assert animalA.is_female == False
        assert animalB.is_female == True

    def test_get_species(self, animalA, animalB):
        assert animalA.species == 'Lion'
        assert animalB.species == 'Koala'

    def test_get_is_native(self, animalA, animalB):
        assert animalA.is_native == False
        assert animalB.is_native == True

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

    def test_set_name(self, animalA, animalB):
        animalA.name = 'Pa'             # Edge case, 2 char min
        assert animalA.name == 'Pa'     # Valid name change
        animalB.name = 'K'              # Invalid input, only 1 char
        animalB.name = 123              # Invalid input, not a string
        assert animalB.name == 'Blinky' # Original name stands

    def test_set_age(self, animalA, animalB):
        animalA.age = 0                 # Edge case, 0 min value
        assert animalA.age == 0         # Valid age change
        animalA.age = 200               # Edge case, 200 max value
        assert animalA.age == 200       # Valid name change
        animalB.age = -1                # Invalid input, less than min
        assert animalB.age == 1         # Original age stands
        animalB.age = 201               # Invalid input, greater than max
        assert animalB.age == 1         # Original age stands
        animalB.age = 'old'             # Invalid input, not an int
        assert animalB.age == 1         # Original age stands
        animalB.age = 10.5              # Invalid input, not an int
        assert animalB.age == 1         # Original age stands

    def test_set_is_female(self, animalA, animalB):
        animalA.is_female = True            # Valid bool input
        assert animalA.is_female == True    # Valid sex change
        animalB.is_female = 'no'            # Invalid input, not bool
        assert animalB.is_female == True    # Original sex stands

    def test_set_species(self, animalA, animalB):
        animalA.species = 'Pelican'         # Valid species name
        assert animalA.species == 'Pelican' # Valid species change
        animalA.species = 'tiger'           # Valid species name, lower case accepted
        assert animalA.species == 'Tiger'   # Valid species change, changed to title case
        animalB.species = 'Tigerrr'         # Invalid input, not in species dict
        assert animalB.species == 'Koala'   # Original species stands

    def test_lookup_functions(self, animalA):
        animalA.species = 'Fairy Penguin'
        assert animalA.species == 'Fairy Penguin'
        assert animalA.is_native == True
        assert animalA.dietary_requirements == 'fish'
        assert animalA.environment == 'Aquatic'
        assert animalA.space == 4

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