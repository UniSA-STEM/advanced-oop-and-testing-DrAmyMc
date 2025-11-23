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
from mammal import Mammal
from bird import Bird


# Dummy staff class for testing enclosure
class DummyStaff:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class TestEnclosure:
    """Testing suite for the Enclosure class."""

    # --- Animal instances for testing ---

    @pytest.fixture
    def animalA(self):
        return Bird('Percy', 2, True, 'Pelican', 2, False)

    @pytest.fixture
    def animalB(self):
        return Mammal('Paddy', 3, False, 'Lion', 'Shaggy')

    @pytest.fixture
    def animalC(self):
        return Bird('Ploppy', 5, False, 'Pelican', 2, False)

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
        return Enclosure('Pelican Palace', 'Aquatic', 25)

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
        assert encB.size == 25

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
        assert encB.calculate_max_animals() == 2
        encB.size = 15
        assert encB.calculate_max_animals() == 1
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

    def test_add_assigned_animal_invalid_environmental_type(self, encB, animalB):
        with pytest.raises(ValueError):
            encB.add_assigned_animal(animalB)

    def test_add_assigned_animal_invalid_animal_type_match(self, encB, animalA):
        encB.animal_type = 'Fairy Penguin'
        with pytest.raises(ValueError):
            encB.add_assigned_animal(animalA)

    def test_add_assigned_animal_invalid_too_small(self, encB, animalA):
        encB.size = 9
        with pytest.raises(ValueError):
            encB.add_assigned_animal(animalA)

    def test_add_assigned_animal_valid_empty_enclosure(self, encB, animalA):
        assert encB.animal_type is None
        assert encB.animals_housed == []
        msg = encB.add_assigned_animal(animalA)
        assert msg == 'You have successfully added a Pelican. This is now a Pelican enclosure.'
        assert encB.animal_type == 'Pelican'
        assert encB.animals_housed == [animalA]

    def test_add_assigned_animal_invalid_too_full(self, encB, animalA, animalC):
        encB.size = 15
        encB.add_assigned_animal(animalA)
        with pytest.raises(ValueError):
            encB.add_assigned_animal(animalC)

    def test_add_assigned_animal_valid_additional_animal(self, encB, animalA, animalC):
        encB.add_assigned_animal(animalA)
        assert encB.animal_type == 'Pelican'
        msg = encB.add_assigned_animal(animalC)
        assert msg == 'You have successfully added another Pelican to this enclosure.'
        assert encB.animals_housed == [animalA, animalC]

    def test_check_capacity_when_empty(self, encB):
        msg = encB.check_capacity()
        assert msg == 'This enclosure is currently empty. It has 25m\u00b2 of space available.'

    def test_check_capacity_more_space_available(self, encB, animalA):
        encB.add_assigned_animal(animalA)
        msg = encB.check_capacity()
        assert msg == 'This enclosure currently houses 1 Pelicans. It has space available for 1 more Pelicans.'

    def test_check_capacity_enclosure_full(self, encB, animalA, animalC):
        encB.add_assigned_animal(animalA)
        encB.add_assigned_animal(animalC)
        msg = encB.check_capacity()
        assert msg == ('This enclosure currently houses 2 Pelicans. It is at maximum capacity and '
                       'has no more space available.')

    def test_list_animals_housed_when_empty(self, encA):
        s = encA.list_animals_housed()
        assert 'ANIMALS HOUSED IN REPTILE HOUSE' in s
        assert 'This enclosure is currently empty.' in s

    def test_list_animals_housed_with_animals(self, encB, animalA, animalC):
        encB.add_assigned_animal(animalA)
        encB.add_assigned_animal(animalC)
        animalC.on_display = False
        s = encB.list_animals_housed()
        assert 'ANIMALS HOUSED IN PELICAN PALACE' in s
        assert 'The Pelicans housed in this enclosure are' in s
        assert 'Percy, Female, aged 2 years, on display' in s
        assert 'Ploppy, Male, aged 5 years, NOT on display' in s

    # --- Testing string display ---

    def test_string_display(self, encA):
        s = str(encA)
        assert 'REPTILE HOUSE' in s
        assert 'Terrarium Enclosure' in s
        assert '20m' in s
        assert '5' in s
        assert 'None' in s
        assert 'This enclosure is currently empty.' in s

    def test_string_display_alt_values(self, encB, keeperA, vetA, animalA, animalC):
        encB.cleanliness_level = 3
        encB.assigned_keeper = keeperA
        encB.assigned_vet = vetA
        encB.add_assigned_animal(animalA)
        encB.add_assigned_animal(animalC)
        s = str(encB)
        assert 'PELICAN PALACE' in s
        assert 'Aquatic Enclosure' in s
        assert '25m' in s
        assert '3' in s
        assert 'Dr Joe Bloggs' in s
        assert 'Zoe Kresta' in s
        assert 'Houses: 2 Pelicans' in s
