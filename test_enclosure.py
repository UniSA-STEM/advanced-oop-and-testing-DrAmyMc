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


class TestEnclosure:
    """Testing suite for the Enclosure class."""

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

    # def test_instantiation_with_invalid_arguments(self):
    #     with pytest.raises(ValueError):
    #         # Invalid name, type, size, and missing argument
    #         Enclosure('R', 'Terrarium', 20)
    #         Enclosure('Reptile House', 'Terrrrarium', 20)
    #         Enclosure('Reptile House', 'Terrarium', 0)
    #         Enclosure('Reptile House', 'Terrarium')

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

    def test_get_on_display(self, encA, encB):
        assert encA.on_display is False
        assert encB.on_display is False

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

#     # --- Modify enclosure attributes to valid values ---
#     enc.name = 'Koala Land'
#     enc.type = 'Bushland'
#     enc.size = 5000
#     enc.cleanliness_level = 0
#     enc.animal_type = 'koala'   # Will automatically convert to title case when matching
#     print(enc)
#
#     # --- Attempt to modify enclosure attributes to invalid values ---
#     enc.name = 'Ba'
#     enc.type = 'Bush'
#     enc.size = 0
#     enc.size = 5001
#     enc.size = 'big'
#     enc.cleanliness_level = -1
#     enc.cleanliness_level = 6
#     enc.cleanliness_level = 'dirty'
#     enc.animal_type = 'Koalaass'
#     print(enc)
#
# def test_report_status():
#     """
#     Direct tests for the Enclosure class for reporting enclosure status based on cleanliness level.
#
#     Tests:
#         - Creation of an enclosure instance.
#         - Manually setting cleanliness level.
#         - Reporting status corresponding to cleanliness.
#     """
#     print("\n=== TEST: Report Enclosure Status ===\n")
#
#     # --- Create and display valid enclosure ---
#     enc = Enclosure("Reptile House", "Terrarium", 20)
#     print(enc)
#
#     # --- Report enclosures statuses for various cleanliness levels ---
#     enc.report_status()
#     enc.cleanliness_level = 4
#     enc.report_status()
#     enc.cleanliness_level = 3
#     enc.report_status()
#     enc.cleanliness_level = 2
#     enc.report_status()
#     enc.cleanliness_level = 1
#     enc.report_status()
#     enc.cleanliness_level = 0
#     enc.report_status()
#
# def test_add_animals():
#     """
#     Direct tests for the Enclosure class for add_animal.
#
#     Tests:
#         - Creating an empty enclosure with no animals.
#         - Adding valid animals and attempting to add invalid animals to enclosure.
#     """
#     print("\n=== TEST: Adding Animal to Enclosure ===\n")
#
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
#
# def test_check_capacity_list_animals():
#     """
#         Direct tests for the Enclosure class for list_animals and check_capacity.
#
#         Tests:
#             - Creating an empty enclosure with no animals listed in list_animals.
#             - Adding animals with updated list_animals and check_capacity displayed.
#         """
#     print("\n=== TEST: Checking Enclosure Capacity and Animal Listing ===\n")
#
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
