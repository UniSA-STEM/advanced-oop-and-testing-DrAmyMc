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

    def test_instantiation_with_invalid_arguments(self):
        with pytest.raises(ValueError):
            Mammal('B', 1, True, 'Koala', 'Short')  # Invalid name
            Mammal('Blinky', 0.5, True, 'Koala', 'Short')  # Invalid age
            Mammal('Blinky', 1, 'yes', 'Koala', 'Short')  # Invalid is_female
            Mammal('Blinky', 1, True, 'Koaaaala', 'Short')  # Invalid species
            Mammal('Blinky', 1, True, 'Koaaaala', 'S')  # Invalid fur type
            Mammal('Blinky', 1, True, 'Koala')  # Missing argument

    # --- Testing getters ---

    def test_get_name(self, mammalA, mammalB):
        assert mammalA.fur_type == 'Shaggy'
        assert mammalB.fur_type == 'Short'

    def test_get_age(self, mammalA, mammalB):
        assert mammalA.is_pregnant is False
        assert mammalB.is_pregnant is False

    # --- Testing setters ---

    def test_set_fur_type(self, mammalA, mammalB):
        """Fur type setter should accept only str of min 3 char."""
        mammalA.fur_type = 'Big'  # Edge case, 3 char min
        assert mammalA.fur_type == 'Big'  # Valid fur type change
        mammalB.fur_type = 'Fur'  # Edge case, 3 char min
        assert mammalB.fur_type == 'Fur'  # Valid fur type change
        with pytest.raises(ValueError):
            mammalB.fur_type = 'Sh'  # Invalid input, only 2 chars
            mammalB.fur_type = 1  # Invalid input, not a string

    def test_set_is_pregnant(self, mammalA, mammalB):
        """Is pregnant setter should accept only true and false and only for females."""
        mammalB.is_pregnant = True  # Valid input for female mammal
        assert mammalB.is_pregnant is True  # Valid pregnancy status change
        mammalB.is_pregnant = False  # Valid input for female mammal
        assert mammalB.is_pregnant is False  # Valid pregnancy status change
        with pytest.raises(ValueError):
            mammalB.is_pregnant = 'Yes'  # Invalid input, not bool value
            mammalB.is_pregnant = 1  # Invalid input, not bool value
            mammalA.is_pregnant = True  # Invalid option for male animal

    # --- Testing behavioural methods ---

    def test_make_sound(self, mammalA):
        s = str(mammalA.make_sound())
        assert 'Paddy' in s
        assert 'Lion' in s
        assert 'rich mammalian noises' in s

    def test_eat(self, mammalA):
        s = str(mammalA.eat())
        assert 'Paddy' in s
        assert 'Lion' in s
        assert 'chews' in s
        assert 'meat' in s

    def test_sleep(self, mammalA):
        s = str(mammalA.sleep())
        assert 'Paddy' in s
        assert 'Lion' in s
        assert 'curls up and goes to sleep' in s

    def test_move(self, mammalA):
        s = str(mammalA.move())
        assert 'Paddy' in s
        assert 'Lion' in s
        assert 'roams around' in s
        assert 'savannah' in s

    def test_string_display(self, mammalA, mammalB):
        s = str(mammalA)
        assert 'PADDY' in s
        assert '3' in s
        assert 'Lion' in s
        assert 'Male' in s
        assert 'meat' in s
        assert 'Savannah' in s
        assert 'not native' in s
        assert '200' in s
        assert 'Pregnancy' not in s
        assert 'Shaggy' in s
        s2 = str(mammalB)
        assert 'Pregnancy' in s2
        assert 'Short' in s2
