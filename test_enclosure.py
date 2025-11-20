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

# Dummy class for testing enclosure
class DummyAnimal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age


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

    def test_instantiation_with_invalid_arguments(self):
        with pytest.raises(ValueError):
            # Invalid name, type, size, and missing argument
            Enclosure('R', 'Terrarium', 20)
            Enclosure('Reptile House', 'Terrrrarium', 20)
            Enclosure('Reptile House', 'Terrarium', 0)
            Enclosure('Reptile House', 'Terrarium')

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

    # --- Testing setters ---

    def test_set_name(self, encA, encB):
        """Name setter should only accept a string of min length 3 char."""
        encA.name = 'Wow'           # Edge case, 3 char min
        assert encA.name == 'Wow'   # Valid name change
        encB.name = 'Lap'           # Edge case, 3 char min
        assert encB.name == 'Lap'   # Valid name change
        with pytest.raises(ValueError):
            encA.name = ''          # Invalid input, empty string
            encA.name = 'La'        # Invalid input, below min char
            encB.name = 123         # Invalid input, not a string

    def test_set_type(self, encA, encB):
        """Type setter should only accept a type from the class type list."""
        encA.type = 'Forest'
        assert encA.type == 'Forest'
        encB.type = 'Aviary'
        assert encB.type == 'Aviary'
        encB.type = 'bushland'          # Will automatically change to title case
        assert encB.type == 'Bushland'
        with pytest.raises(ValueError):
            encA.type = ''              # Invalid input, empty string
            encA.type = 1               # Invalid input, integer
            encB.type = 'Tundra'        # Invalid input, not in type list

    def test_set_size(self, encA, encB):
        """Size setter should only accept integers between 1 and 5000."""
        encA.size = 5000 # Edge case, max value
        assert encA.size == 5000
        encB.size = 1   # Edge case, min value
        assert encB.size == 1
        with pytest.raises(ValueError):
            encA.size = 0       # below min
            encA.size = 5001    # above max
            encA.size = -10     # negative
            encA.size = 100.5   # float
            encB.size = 'big'   # str

    def test_set_cleanliness_level(self, encA, encB):
        """Cleanliness level setter should only accept integers between 0 and 5."""
        encA.cleanliness_level = 3          # Change level from default
        assert encA.cleanliness_level == 3
        encA.cleanliness_level = 5          # Edge case, max value
        assert encA.cleanliness_level == 5
        encB.cleanliness_level = 0
        assert encB.cleanliness_level == 0  # Edge case, min value
        with pytest.raises(ValueError):
            encA.cleanliness_level = 6  # above max
            encA.cleanliness_level = -1 # negative, below min
            encA.cleanliness_level = 3.5 # float
            encB.cleanliness_level = 'dirty'    # str

    def test_set_on_display(self, encA, encB):
        """On display setter should only accept bool values."""
        encA.on_display = True
        assert encA.on_display is True
        encB.on_display = True
        assert encB.on_display is True
        encB.on_display = False
        assert encB.on_display is False
        with pytest.raises(ValueError):
            encA.on_display = 'yes'
            encB.on_display = 1

    def test_set_animal_type(self, encA, encB):
        """Animal type setter should accept only values found in species dictionary (any case)."""
        encA.animal_type = 'Pelican'
        assert encA.animal_type == 'Pelican'
        encB.animal_type = 'tiger'  # Valid species name, lower case accepted
        assert encB.animal_type == 'Tiger'  # Valid animal type, changed to title case
        with pytest.raises(ValueError):
            encA.animal_type = 'Tigerrr'  # Invalid input, not in species dict
            encB.animal_type = 1  # Invalid input, not in species dict

    def test_set_assigned_keeper(self, encA, encB):
        encA.assigned_keeper = 'Joe Bloggs'
        assert encA.assigned_keeper == 'Joe Bloggs'
        encB.assigned_keeper = 'Zoe Bloggs'
        assert encB.assigned_keeper == 'Zoe Bloggs'

    def test_set_assigned_vet(self, encA, encB):
        encA.assigned_vet = 'Joe Bloggs'
        assert encA.assigned_vet == 'Joe Bloggs'
        encB.assigned_vet = 'Zoe Bloggs'
        assert encB.assigned_vet == 'Zoe Bloggs'

    # --- Testing helper methods ---

    def test_calculate_max_animals(self, encB):
        assert encB.calculate_max_animals() is None
        encB.animal_type = 'Pelican'
        assert encB.calculate_max_animals() == 3
        encB.size = 25
        assert encB.calculate_max_animals() == 2
        encB.size = 9
        assert encB.calculate_max_animals() == 0

    def test_be_cleaned(self, encA, encB):
        encA.cleanliness_level = 3
        assert encA.cleanliness_level == 3
        encB.cleanliness_level = 0
        assert encB.cleanliness_level == 0
        encA.be_cleaned()
        assert encA.cleanliness_level == 5
        encB.be_cleaned()
        assert encB.cleanliness_level == 5

    # --- Testing behavioural methods ---

    def test_report_status(self, encA):
        encA.report_status() == 'This enclosure is pristine. It has just been cleaned.'
        encA.cleanliness_level = 4
        encA.report_status() == 'This enclosure is quite clean. It does not need cleaning yet.'
        encA.cleanliness_level = 3
        encA.report_status() == 'This enclosure is becoming dirty. It should be cleaned soon.'
        encA.cleanliness_level = 2
        encA.report_status() == 'This enclosure is now dirty. It should be cleaned now.'
        encA.cleanliness_level = 1
        encA.report_status() == 'This enclosure is very dirty. It should be cleaned urgently.'
        encA.cleanliness_level = 0
        encA.report_status() == 'This enclosure is filthy. Immediate action is required.'

    def test_become_poopy_when_empty(self, encB):
        encB.become_poopy()
        assert encB.cleanliness_level == 5  # Cleanliness level will not reduce when no animals present

    def test_become_poopy_with_animals(self, encB):
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
        encB.become_poopy()
        assert encB.cleanliness_level == 0  # Cleanliness cannot reduce below 0

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
