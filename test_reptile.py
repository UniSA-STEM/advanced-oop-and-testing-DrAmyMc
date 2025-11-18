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

    def test_instantiation_with_invalid_arguments(self):
        with pytest.raises(ValueError):
            # Invalid name, age, is_female, species name, min_temp, is_venomous, and missing argument
            Reptile("L", 1, False, "Lace Monitor", 18, False)
            Reptile("Lizzie", 0.5, False, "Lace Monitor", 18, False)
            Reptile("Lizzie", 1, 'yes', "Lace Monitor", 18, False)
            Reptile("Lizzie", 1, False, "Snake", 18, False)
            Reptile("Lizzie", 1, False, "Lace Monitor", 10, False)
            Reptile("Lizzie", 1, False, "Lace Monitor", 18, 'no')
            Reptile("Lizzie", 1, False, "Lace Monitor", 18)

    # --- Testing getters ---

    def test_get_min_temp(self, reptileA, reptileB):
        assert reptileA.min_temp == 18
        assert reptileB.min_temp == 21

    def test_get_is_venomous(self, reptileA, reptileB):
        assert reptileA.is_venomous is False
        assert reptileB.is_venomous is True

    # --- Testing setters ---

    def test_set_min_temp(self, reptileA, reptileB):
        """Min temp setter should accept only an int between 15 and 25."""
        reptileA.min_temp = 15  # Edge case, 15 min
        assert reptileA.min_temp == 15  # Valid min_temp change
        reptileB.min_temp = 25  # Edge case, 25 max
        assert reptileB.min_temp == 25  # Valid min_temp change
        with pytest.raises(ValueError):
            reptileA.min_temp = 14  # Invalid input, below min value (edge)
            reptileA.min_temp = 26  # Invalid input, above max value (edge)
            reptileB.min_temp = -20  # Invalid input, negative value
            reptileB.min_temp = 'low'  # Invalid input, not an int
            reptileB.min_temp = 20.1  # Invalid input, not an int

    def test_set_is_venomous(self, reptileA, reptileB):
        """Is venomous setter should accept only true and false."""
        reptileA.is_venomous = True  # Valid input
        assert reptileA.is_venomous is True  # Valid status change
        reptileB.is_venomous = False  # Valid input
        assert reptileB.is_venomous is False  # Valid status change
        with pytest.raises(ValueError):
            reptileA.is_venomous = 'Yes'  # Invalid input, not bool value
            reptileB.is_venomous = 1  # Invalid input, not bool value

    # --- Testing behavioural methods ---

    def test_make_sound(self, reptileA):
        s = str(reptileA.make_sound())
        assert 'Lizzie' in s
        assert 'Lace Monitor' in s
        assert 'reptilian' in s

    def test_eat(self, reptileA):
        s = str(reptileA.eat())
        assert 'Lizzie' in s
        assert 'Lace Monitor' in s
        assert 'slowly feeds' in s
        assert 'insects' in s

    def test_sleep(self, reptileA):
        s = str(reptileA.sleep())
        assert 'Lizzie' in s
        assert 'Lace Monitor' in s
        assert 'becomes still and rests' in s

    def test_move(self, reptileA):
        s = str(reptileA.move())
        assert 'Lizzie' in s
        assert 'Lace Monitor' in s
        assert 'moves slowly' in s
        assert 'terrarium' in s

    def test_bask(self, reptileA):
        s = str(reptileA.bask())
        assert 'Lizzie' in s
        assert 'Lace Monitor' in s
        assert 'basks in the heat' in s

    def test_lay_eggs(self, reptileA, reptileB):
        s = str(reptileB.lay_eggs())  # Female can lay eggs
        assert 'Hissy' in s
        assert 'Brown Snake' in s
        assert 'lays eggs' in s
        s2 = str(reptileA.lay_eggs())  # Male cannot lay eggs
        assert 'Lizzie' in s2
        assert 'cannot lay' in s2
        assert 'they are male' in s2

    def test_string_display(self, reptileA, reptileB):
        s = str(reptileA)
        assert 'LIZZIE' in s
        assert '1' in s
        assert 'Lace Monitor' in s
        assert 'Male' in s
        assert 'insects' in s
        assert 'Terrarium' in s
        assert 'native' in s
        assert '18' in s
        assert 'Safe to handle' in s
        s2 = str(reptileB)
        assert 'Female' in s2
        assert 'venomous' in s2
        assert 'Handle with care' in s2
