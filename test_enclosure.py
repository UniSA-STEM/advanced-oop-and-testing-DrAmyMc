"""
File: test_enclosure.py
Description: Testing suite for the Enclosure class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from enclosure import Enclosure


# Dummy animal class for testing enclosure
class DummyAnimal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age


# Dummy staff class for testing enclosure
class DummyStaff:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class TestEnclosure:
    """Testing suite for the Enclosure class."""

    # --- Dummy Animal instances for testing ---

    @pytest.fixture
    def animalA(self):
        return DummyAnimal('Percy', 'Pelican', 2)

    # --- Dummy Staff instances for testing ---

    @pytest.fixture
    def vetA(self):
        return DummyStaff('Joe', 'Bloggs')

    @pytest.fixture
    def keeperA(self):
        return DummyStaff('Zoe', 'Kresta')

    # --- Enclosure instances for testing ---

    @pytest.fixture
    def encA(self):
        return Enclosure('Reptile House', 'Terrarium', 20)

    @pytest.fixture
    def encB(self):
        return Enclosure('Pelican Palace', 'Aquatic', 30)

    @pytest.fixture
    def encC(self):
        return Enclosure('Small Savannah', 'Savannah', 150)

    # --- Testing invalid instantiation ---

    def test_instantiation_with_missing_argument(self):
        with pytest.raises(TypeError):
            Enclosure('Reptile House', 'Terrarium')

    def test_instantiation_with_invalid_name(self):
        with pytest.raises(ValueError):
            Enclosure('R', 'Terrarium', 20)

    def test_instantiation_with_invalid_type(self):
        with pytest.raises(ValueError):
            Enclosure('Reptile House', 'Terrrrarium', 20)

    def test_instantiation_with_invalid_size(self):
        with pytest.raises(ValueError):
            Enclosure('Reptile House', 'Terrarium', 0)

    # --- Testing getters ---

    def test_get_name(self, encA, encB):
        assert encA.name == 'Reptile House'
        assert encB.name == 'Pelican Palace'

    def test_get_type(self, encA, encB):
        assert encA.type == 'Terrarium'
        assert encB.type == 'Aquatic'

    def test_get_size(self, encA, encB):
        assert encA.size == 20
        assert encB.size == 30

    def test_get_cleanliness_level(self, encA, encB):
        assert encA.cleanliness_level == 5
        assert encB.cleanliness_level == 5

    def test_get_animal_type(self, encA, encB):
        assert encA.animal_type is None
        assert encB.animal_type is None

    def test_get_animals_housed(self, encA, encB):
        assert encA.animals_housed == []
        assert encB.animals_housed == []

    def test_get_assigned_keeper(self, encA, encB):
        assert encA.assigned_keeper is None
        assert encB.assigned_keeper is None

    def test_get_assigned_vet(self, encA, encB):
        assert encA.assigned_vet is None
        assert encB.assigned_vet is None

    # --- Testing setters ---

    def test_set_name_valid_min_length(self, encA):
        encA.name = 'Wow'
        assert encA.name == 'Wow'

    def test_set_name_invalid_short_str(self, encA):
        with pytest.raises(ValueError):
            encA.name = 'La'

    def test_set_name_invalid_input_type_bool(self, encA):
        with pytest.raises(ValueError):
            encA.name = False

    def test_set_type_valid_exact(self, encA):
        encA.type = 'Forest'
        assert encA.type == 'Forest'

    def test_set_type_valid_lower_case(self, encA):
        encA.type = 'bushland'
        assert encA.type == 'Bushland'

    def test_set_type_invalid_not_in_list(self, encA):
        with pytest.raises(ValueError):
            encA.type = 'Tundra'

    def test_set_type_invalid_input_int(self, encA):
        with pytest.raises(ValueError):
            encA.type = 1

    def test_set_size_valid_min_size(self, encA):
        encA.size = 1
        assert encA.size == 1

    def test_set_size_valid_max_size(self, encA):
        encA.size = 5000
        assert encA.size == 5000

    def test_set_size_invalid_below_min(self, encA):
        with pytest.raises(ValueError):
            encA.size = 0

    def test_set_size_invalid_above_max(self, encA):
        with pytest.raises(ValueError):
            encA.size = 5001

    def test_set_size_invalid_input_type_float(self, encA):
        with pytest.raises(ValueError):
            encA.size = 100.5

    def test_set_size_invalid_input_type_bool(self, encA):
        with pytest.raises(ValueError):
            encA.size = True

    def test_set_cleanliness_level_valid_min_level(self, encA):
        encA.cleanliness_level = 0
        assert encA.cleanliness_level == 0

    def test_set_cleanliness_level_valid_max_level(self, encA):
        encA.cleanliness_level = 3  # Change level from default
        assert encA.cleanliness_level == 3
        encA.cleanliness_level = 5
        assert encA.cleanliness_level == 5

    def test_set_cleanliness_level_invalid_below_min(self, encA):
        with pytest.raises(ValueError):
            encA.cleanliness_level = -1

    def test_set_cleanliness_level_invalid_above_max(self, encA):
        with pytest.raises(ValueError):
            encA.cleanliness_level = 6

    def test_set_cleanliness_level_invalid_input_type_float(self, encA):
        with pytest.raises(ValueError):
            encA.cleanliness_level = 3.5

    def test_set_cleanliness_level_invalid_input_type_bool(self, encA):
        with pytest.raises(ValueError):
            encA.cleanliness_level = False

    def test_set_animal_type_valid_exact_case(self, encA):
        encA.animal_type = 'Pelican'
        assert encA.animal_type == 'Pelican'

    def test_set_animal_type_valid_lower_case(self, encA):
        encA.animal_type = 'tiger'
        assert encA.animal_type == 'Tiger'

    def test_set_animal_type_valid_return_to_empty(self, encA):
        encA.animal_type = 'Pelican'
        assert encA.animal_type == 'Pelican'
        encA.animal_type = None
        assert encA.animal_type is None

    def test_set_animal_type_invalid_not_in_dict(self, encA):
        with pytest.raises(ValueError):
            encA.animal_type = 'Tigerrr'

    def test_set_animal_type_invalid_input_type_bool(self, encA):
        with pytest.raises(ValueError):
            encA.animal_type = False

    def test_set_assigned_keeper_valid(self, encA, keeperA):
        encA.assigned_keeper = keeperA
        assert encA.assigned_keeper is keeperA

    def test_set_assigned_vet_valid(self, encA, vetA):
        encA.assigned_vet = vetA
        assert encA.assigned_vet is vetA

    # --- Testing helper methods ---

    def test_calculate_max_animals_valid_no_animal_type(self, encB):
        assert encB.calculate_max_animals() is None

    def test_calculate_max_animals_valid(self, encB):
        encB.animal_type = 'Pelican'
        assert encB.calculate_max_animals() == 3
        encB.size = 25
        assert encB.calculate_max_animals() == 2
        encB.size = 9
        assert encB.calculate_max_animals() == 0

    def test_be_cleaned_valid_cleanliness_level0(self, encA):
        encA.cleanliness_level = 0
        encA.be_cleaned()
        assert encA.cleanliness_level == 5

    def test_be_cleaned_valid_cleanliness_level3(self, encA):
        encA.cleanliness_level = 3
        encA.be_cleaned()
        assert encA.cleanliness_level == 5

    def test_be_cleaned_valid_cleanliness_level5(self, encA):
        encA.be_cleaned()
        assert encA.cleanliness_level == 5

    def test_lookup_feed_valid_no_animal_type(self, encA):
        assert encA.lookup_feed() is None

    def test_lookup_feed_valid_animal(self, encB):
        encB.animal_type = 'Pelican'
        assert encB.lookup_feed() == 'fish'

    # --- Testing behavioural methods ---

    def test_report_status_cleanliness_level5(self, encA):
        assert encA.report_status() == 'This enclosure is pristine. It has just been cleaned.'

    def test_report_status_cleanliness_level4(self, encA):
        encA.cleanliness_level = 4
        assert encA.report_status() == 'This enclosure is quite clean. It does not need cleaning yet.'

    def test_report_status_cleanliness_level3(self, encA):
        encA.cleanliness_level = 3
        assert encA.report_status() == 'This enclosure is becoming dirty. It should be cleaned soon.'

    def test_report_status_cleanliness_level2(self, encA):
        encA.cleanliness_level = 2
        assert encA.report_status() == 'This enclosure is now dirty. It should be cleaned now.'

    def test_report_status_cleanliness_level1(self, encA):
        encA.cleanliness_level = 1
        assert encA.report_status() == 'This enclosure is very dirty. It should be cleaned urgently.'

    def test_report_status_cleanliness_level0(self, encA):
        encA.cleanliness_level = 0
        assert encA.report_status() == 'This enclosure is filthy. Immediate action is required.'

    def test_become_poopy_when_empty_still_level5(self, encA):
        assert encA.become_poopy() == 'Reptile House has no animals in the enclosure to poop in it.'
        assert encA.cleanliness_level == 5

    def test_become_poopy_with_animals_reduce_by_one_level(self, encB):
        encB.animal_type = 'Pelican'
        encB.become_poopy()
        assert encB.cleanliness_level == 4
        encB.become_poopy()
        assert encB.cleanliness_level == 3
        encB.become_poopy()
        assert encB.cleanliness_level == 2
        encB.become_poopy()
        assert encB.cleanliness_level == 1
        encB.become_poopy()
        assert encB.cleanliness_level == 0

    def test_become_poopy_with_animals_cannot_go_below_zero(self, encB):
        encB.animal_type = 'Pelican'
        encB.cleanliness_level = 0
        encB.become_poopy()
        assert encB.cleanliness_level == 0

    def test_become_poopy_with_animals_return_message(self, encB):
        encB.animal_type = 'Pelican'
        assert 'Pelican Palace is becoming dirtier as the Pelicans poop.' in encB.become_poopy()
        assert 'This enclosure is becoming dirty. It should be cleaned soon.' in encB.become_poopy()
        assert 'Pelican Palace is becoming dirtier as the Pelicans poop.' in encB.become_poopy()
        assert 'This enclosure is very dirty. It should be cleaned urgently.' in encB.become_poopy()

    def test_list_animals_when_empty(self, encA, encB):
        assert encA.list_animals() == 'Reptile House is currently empty.\n'
        assert encB.list_animals() == 'Pelican Palace is currently empty.\n'

    # def test_list_animals_with_animals(self, encB):
    #     a1 = DummyAnimal("Pelly", "Pelican", 5)
    #     a2 = DummyAnimal("Percy", "Pelican", 2)
    #     a3 = DummyAnimal("Pedro", "Pelican", 1)
    #     encB.animals_housed = [a1, a2, a3]  THIS WON"T WORK ADD ANIMALS FIRST NOT A SETTER
    #     s = encB.list_animals()
    #     assert 'Pelican Palace' in s

#
# def test_check_capacity_list_animals():
#     # --- Create and display empty enclosure ---
#     enc = Enclosure("Test Enclosure", "Aquatic", 30)
#     print(enc)
#     enc.list_animals()
#     enc.check_capacity()
#
#     # --- Create test animals ---
#     bird1 = Bird("Percy1", 2, "Pelican")
#     bird2 = Bird("Percy2", 2, "Pelican")
#     bird3 = Bird("Percy3", 2, "Pelican")
#
#     # --- Add animals, list animals and check capacity ---
#     enc.add_animal(bird1)
#     enc.list_animals()
#     enc.check_capacity()
#     enc.add_animal(bird2)
#     enc.list_animals()
#     enc.check_capacity()
#     enc.add_animal(bird3)
#     enc.list_animals()
#     enc.check_capacity()
#
# def test_add_animals():
#     # --- Create and display valid enclosure and animals ---
#     enc = Enclosure("Test Enclosure", "Aquatic", 30)
#     print(enc)
#     person = Veterinarian("Test Vet", 2025)
#     bird1 = Bird("Percy1", 2, "Pelican")
#     bird2 = Bird("Percy2", 2, "Pelican")
#     bird3 = Bird("Percy3", 2, "Pelican")
#     bird4 = Bird("Percy4", 2, "Pelican")
#     cat = Mammal("Puddy", 3, "Lion")
#     otter = Mammal("Otty", 1, "Otter")
#
#     # --- Add valid and attempt to add invalid selections to enclosure --
#     enc.add_animal(person)      # Not a valid animal object
#     enc.add_animal(cat)         # Not an environmental match
#     enc.add_animal(bird1)       # Valid addition, sets enclosure to Pelican
#     enc.add_animal(otter)       # Not the correct species
#     enc.add_animal(bird2)       # Valid addition
#     enc.add_animal(bird3)       # Valid addition
#     enc.add_animal(bird4)       # No more space in enclosure
#     print(enc)                  # Enclosure will now contain 3 pelicans
