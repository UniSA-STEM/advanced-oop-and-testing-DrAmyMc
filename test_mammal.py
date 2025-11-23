"""
File: test_mammal.py
Description: Testing suite for the Mammal child class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from mammal import Mammal


class TestMammal:
    """Testing suite for the Mammal child class of Animal parent class."""

    # --- Mammal instances for testing ---

    @pytest.fixture
    def mammalA(self):
        return Mammal('Paddy', 3, False, 'Lion', 'Shaggy')

    @pytest.fixture
    def mammalB(self):
        return Mammal('Blinky', 1, True, 'Koala', 'Short')

    # --- Testing invalid instantiation ---

    def test_instantiation_with_missing_argument(self):
        with pytest.raises(TypeError):
            Mammal('Blinky', 1, True, 'Koala')

    def test_instantiation_with_invalid_name(self):
        with pytest.raises(ValueError):
            Mammal('B', 1, True, 'Koala', 'Short')  # Invalid name

    def test_instantiation_with_invalid_age(self):
        with pytest.raises(ValueError):
            Mammal('Blinky', 0.5, True, 'Koala', 'Short')

    def test_instantiation_with_invalid_is_female(self):
        with pytest.raises(ValueError):
            Mammal('Blinky', 1, 'yes', 'Koala', 'Short')

    def test_instantiation_with_invalid_species(self):
        with pytest.raises(ValueError):
            Mammal('Blinky', 1, True, 'Koaaaala', 'Short')

    def test_instantiation_with_invalid_fur_type(self):
        with pytest.raises(ValueError):
            Mammal('Blinky', 1, True, 'Koaaaala', 'S')

    # --- Testing getters ---

    def test_get_fur_type(self, mammalA, mammalB):
        assert mammalA.fur_type == 'Shaggy'
        assert mammalB.fur_type == 'Short'

    def test_get_is_pregnant(self, mammalA, mammalB):
        assert mammalA.is_pregnant is False
        assert mammalB.is_pregnant is False

    # --- Testing setters ---

    def test_set_fur_type_valid(self, mammalA):
        mammalA.fur_type = 'Fur'
        assert mammalA.fur_type == 'Fur'

    def test_set_fur_type_invalid_short_string(self, mammalA):
        with pytest.raises(ValueError):
            mammalA.fur_type = 'F'

    def test_set_fur_type_invalid_input_type_int(self, mammalA):
        with pytest.raises(ValueError):
            mammalA.fur_type = 123

    def test_set_fur_type_invalid_input_type_bool(self, mammalA):
        with pytest.raises(ValueError):
            mammalA.fur_type = False

    def test_set_is_pregnant_valid(self, mammalB):
        mammalB.is_pregnant = True
        assert mammalB.is_pregnant is True
        mammalB.is_pregnant = False
        assert mammalB.is_pregnant is False

    def test_set_is_pregnant_invalid_male(self, mammalA):
        with pytest.raises(ValueError):
            mammalA.is_pregnant = True

    def test_set_is_pregnant_invalid_input_type_int(self, mammalB):
        with pytest.raises(ValueError):
            mammalB.is_pregnant = 1

    # --- Testing behavioural methods ---

    def test_make_sound(self, mammalA):
        assert mammalA.make_sound() == 'Paddy the Lion makes low, rich mammalian noises.'

    def test_eat(self, mammalA):
        assert mammalA.eat() == 'Paddy the Lion chews on their meat.'

    def test_sleep(self, mammalA):
        assert mammalA.sleep() == 'Paddy the Lion curls up and goes to sleep.'

    def test_move(self, mammalA):
        assert mammalA.move() == 'Paddy the Lion roams around their savannah enclosure.'

    # --- Testing string display ---

    def test_string_display_male(self, mammalA):
        s = str(mammalA)
        assert 'PADDY' in s
        assert 'MAMMAL' in s
        assert 'Pregnancy status' not in s
        assert 'Shaggy' in s

    def test_string_display_female_not_pregnant(self, mammalB):
        s = str(mammalB)
        assert 'Pregnancy status' in s
        assert 'Not pregnant' in s
        assert 'Short' in s

    def test_string_display_female_pregnant(self, mammalB):
        mammalB.is_pregnant = True
        s = str(mammalB)
        assert 'PREGNANT' in s
