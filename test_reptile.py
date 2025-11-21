"""
File: test_reptile.py
Description: Testing suite for the Reptile child class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from reptile import Reptile


class TestReptile:
    """Testing suite for the Reptile child class of Animal parent class."""

    # --- Reptile instances for testing ---

    @pytest.fixture
    def reptileA(self):
        return Reptile("Lizzie", 1, False, "Lace Monitor", 18, False)

    @pytest.fixture
    def reptileB(self):
        return Reptile('Hissy', 3, True, 'Brown Snake', 21, True)

    # --- Testing invalid instantiation ---

    def test_instantiation_with_missing_argument(self):
        with pytest.raises(TypeError):
            Reptile("Lizzie", 1, False, "Lace Monitor", 18)

    def test_instantiation_with_invalid_name(self):
        with pytest.raises(ValueError):
            Reptile("L", 1, False, "Lace Monitor", 18, False)

    def test_instantiation_with_invalid_age(self):
        with pytest.raises(ValueError):
            Reptile("Lizzie", 0.5, False, "Lace Monitor", 18, False)

    def test_instantiation_with_invalid_is_female(self):
        with pytest.raises(ValueError):
            Reptile("Lizzie", 1, 'yes', "Lace Monitor", 18, False)

    def test_instantiation_with_invalid_species(self):
        with pytest.raises(ValueError):
            Reptile("Lizzie", 1, False, "Snake", 18, False)

    def test_instantiation_with_invalid_min_temp(self):
        with pytest.raises(ValueError):
            Reptile("Lizzie", 1, False, "Lace Monitor", 10, False)

    def test_instantiation_with_invalid_venomous(self):
        with pytest.raises(ValueError):
            Reptile("Lizzie", 1, False, "Lace Monitor", 18, 'no')

    # --- Testing getters ---

    def test_get_min_temp(self, reptileA, reptileB):
        assert reptileA.min_temp == 18
        assert reptileB.min_temp == 21

    def test_get_is_venomous(self, reptileA, reptileB):
        assert reptileA.is_venomous is False
        assert reptileB.is_venomous is True

    # --- Testing setters ---

    def test_set_min_temp_valid_min_value(self, reptileA):
        reptileA.min_temp = 15
        assert reptileA.min_temp == 15

    def test_set_min_temp_valid_max_value(self, reptileA):
        reptileA.min_temp = 25
        assert reptileA.min_temp == 25

    def test_set_min_temp_invalid_below_min(self, reptileA):
        with pytest.raises(ValueError):
            reptileA.min_temp = 14

    def test_set_min_temp_invalid_above_max(self, reptileA):
        with pytest.raises(ValueError):
            reptileA.min_temp = 26

    def test_set_min_temp_invalid_input_float(self, reptileA):
        with pytest.raises(ValueError):
            reptileA.min_temp = 20.5

    def test_set_min_temp_invalid_input_bool(self, reptileA):
        with pytest.raises(ValueError):
            reptileA.min_temp = False

    def test_set_is_venomous_valid(self, reptileA, reptileB):
        reptileA.is_venomous = True
        assert reptileA.is_venomous is True
        reptileB.is_venomous = False
        assert reptileB.is_venomous is False

    def test_set_is_venomous_invalid_input_int(self, reptileA):
        with pytest.raises(ValueError):
            reptileA.is_venomous = 1

    # --- Testing behavioural methods ---

    def test_make_sound(self, reptileA):
        assert reptileA.make_sound() == 'Lizzie the Lace Monitor makes a soft reptilian sound.'

    def test_eat(self, reptileA):
        assert reptileA.eat() == 'Lizzie the Lace Monitor slowly feeds on their insects.'

    def test_sleep(self, reptileA):
        assert reptileA.sleep() == 'Lizzie the Lace Monitor becomes still and rests in a sheltered spot.'

    def test_move(self, reptileA):
        assert reptileA.move() == 'Lizzie the Lace Monitor moves slowly about their terrarium enclosure.'

    def test_bask(self, reptileA):
        assert reptileA.bask() == 'Lizzie the Lace Monitor basks in the heat to warm their core temperature.'

    def test_lay_eggs_valid_female(self, reptileB):
        assert reptileB.lay_eggs() == 'Hissy the Brown Snake lays eggs.'

    def test_lay_eggs_invalid_male(self, reptileA):
        assert reptileA.lay_eggs() == 'Lizzie cannot lay eggs because he is male.'

    # --- Testing string display ---

    def test_string_display_not_venomous(self, reptileA):
        s = str(reptileA)
        assert 'LIZZIE' in s
        assert 'REPTILE' in s
        assert 'Minimum temperature' in s
        assert '18' in s
        assert 'Safe to handle - not venomous' in s

    def test_string_display_venomous(self, reptileB):
        s = str(reptileB)
        assert '21' in s
        assert 'Handle with care - VENOMOUS' in s