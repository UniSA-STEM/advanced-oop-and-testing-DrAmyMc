"""
File: test_animal.py
Description: Testing suite for the abstract Animal parent class.
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


class DummyHealthRecord:
    """Dummy record class for testing add/check health record functionality."""

    def __init__(self, is_current):
        self.is_current = is_current


class TestAnimal:
    """Testing suite for the abstract Animal class via DummyAnimal test class."""

    # --- Animal instances for testing ---

    @pytest.fixture
    def animalA(self):
        return DummyAnimal('Paddy', 3, False, 'Lion')

    @pytest.fixture
    def animalB(self):
        return DummyAnimal('Blinky', 1, True, 'Koala')

    # --- Testing invalid instantiation ---

    def test_abstract_class_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            Animal('Blinky', 1, True, 'Koala')

    def test_instantiation_with_missing_argument(self):
        with pytest.raises(TypeError):
            DummyAnimal('Blinky', 1, True)

    def test_instantiation_with_invalid_name(self):
        with pytest.raises(ValueError):
            DummyAnimal('B', 1, True, 'Koala')

    def test_instantiation_with_invalid_age(self):
        with pytest.raises(ValueError):
            DummyAnimal('Blinky', 0.5, True, 'Koala')

    def test_instantiation_with_invalid_is_female(self):
        with pytest.raises(ValueError):
            DummyAnimal('Blinky', 1, 'yes', 'Koala')

    def test_instantiation_with_invalid_species(self):
        with pytest.raises(ValueError):
            DummyAnimal('Blinky', 1, True, 'Koaaaala')

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

    def test_get_on_display(self, animalA, animalB):
        assert animalA.on_display is True
        assert animalB.on_display is True

    # --- Testing setters ---

    def test_set_name_valid(self, animalA):
        animalA.name = 'Pa'
        assert animalA.name == 'Pa'

    def test_set_name_invalid_short_string(self, animalA):
        with pytest.raises(ValueError):
            animalA.name = 'K'

    def test_set_name_invalid_input_type_int(self, animalA):
        with pytest.raises(ValueError):
            animalA.name = 123

    def test_set_name_invalid_input_type_bool(self, animalA):
        with pytest.raises(ValueError):
            animalA.name = False

    def test_set_age_valid(self, animalA):
        animalA.age = 0
        assert animalA.age == 0
        animalA.age = 200
        assert animalA.age == 200

    def test_set_age_invalid_below_min(self, animalA):
        with pytest.raises(ValueError):
            animalA.age = -1

    def test_set_age_invalid_above_max(self, animalA):
        with pytest.raises(ValueError):
            animalA.age = 201

    def test_set_age_invalid_input_type_float(self, animalA):
        with pytest.raises(ValueError):
            animalA.age = 2.5

    def test_set_age_invalid_input_type_bool(self, animalA):
        with pytest.raises(ValueError):
            animalA.age = False

    def test_set_is_female_valid(self, animalA, animalB):
        animalA.is_female = True
        assert animalA.is_female is True
        animalB.is_female = False
        assert animalB.is_female is False

    def test_set_is_female_invalid_input_type_int(self, animalA):
        with pytest.raises(ValueError):
            animalA.is_female = 1

    def test_set_species_valid(self, animalA):
        animalA.species = 'Pelican'
        assert animalA.species == 'Pelican'

    def test_set_species_valid_case_change(self, animalA):
        animalA.species = 'tiger'
        assert animalA.species == 'Tiger'

    def test_set_species_invalid_species_name(self, animalA):
        with pytest.raises(ValueError):
            animalA.species = 'Tigerrr'

    def test_set_species_invalid_input_type_int(self, animalA):
        with pytest.raises(ValueError):
            animalA.species = 1

    def test_set_on_display_valid(self, animalA):
        animalA.on_display = False
        assert animalA.on_display is False

    def test_set_on_display_invalid_input_int(self, animalA):
        with pytest.raises(ValueError):
            animalA.on_display = 1

    # --- Testing lookup methods ---

    def test_lookup_is_native(self, animalA):
        animalA.species = 'Fairy Penguin'
        assert animalA.species == 'Fairy Penguin'
        # Value will be automatically updated to Fairy Penguin value due to lookup functions
        assert animalA.is_native is True

    def test_lookup_diet(self, animalA):
        animalA.species = 'Fairy Penguin'
        assert animalA.species == 'Fairy Penguin'
        # Value will be automatically updated to Fairy Penguin value due to lookup functions
        assert animalA.dietary_requirements == 'fish'

    def test_lookup_environment(self, animalA):
        animalA.species = 'Fairy Penguin'
        assert animalA.species == 'Fairy Penguin'
        # Value will be automatically updated to Fairy Penguin value due to lookup functions
        assert animalA.environment == 'Aquatic'

    def test_lookup_space(self, animalA):
        animalA.species = 'Fairy Penguin'
        assert animalA.species == 'Fairy Penguin'
        # Value will be automatically updated to Fairy Penguin value due to lookup functions
        assert animalA.space == 4

    # --- Testing helper methods ---

    def test_add_health_record_single(self, animalA):
        recordA = DummyHealthRecord(True)
        animalA.add_health_record(recordA)
        assert animalA.health_record == [recordA]

    def test_add_health_record_multiple(self, animalA):
        recordA = DummyHealthRecord(False)
        recordB = DummyHealthRecord(False)
        recordC = DummyHealthRecord(True)
        animalA.add_health_record(recordA)
        animalA.add_health_record(recordB)
        animalA.add_health_record(recordC)
        assert animalA.health_record == [recordA, recordB, recordC]

    def test_lookup_current_record_exists(self, animalA):
        recordA = DummyHealthRecord(False)
        recordB = DummyHealthRecord(False)
        recordC = DummyHealthRecord(True)
        animalA.add_health_record(recordA)
        animalA.add_health_record(recordB)
        animalA.add_health_record(recordC)
        assert animalA.lookup_current_record() is recordC

    def test_lookup_current_record_none_current(self, animalA):
        recordA = DummyHealthRecord(False)
        recordB = DummyHealthRecord(False)
        recordC = DummyHealthRecord(False)
        animalA.add_health_record(recordA)
        animalA.add_health_record(recordB)
        animalA.add_health_record(recordC)
        assert animalA.lookup_current_record() is None

    def test_lookup_current_record_no_records(self, animalA):
        assert animalA.lookup_current_record() is None

    # --- Testing string display ---

    def test_string_display(self, animalA):
        s = str(animalA)
        assert 'PADDY' in s
        assert 'DUMMYANIMAL' in s
        assert 'Lion' in s
        assert 'not native' in s
        assert 'Currently on display' in s
        assert '3' in s
        assert 'Male' in s
        assert 'Savannah' in s
        assert '200' in s
        assert 'Meat' in s

    def test_string_display_alt_values(self, animalB):
        animalB.on_display = False
        s = str(animalB)
        assert 'is native' in s
        assert 'NOT on display' in s
        assert 'Female' in s

    # --- Testing behavioural methods from abstract methods ---

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
