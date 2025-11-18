"""
File: test_bird.py
Description: Testing suite for the Bird child class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from bird import Bird


class TestBird:
    """Testing suite for the Bird child class of Animal parent class."""

    # --- Bird instances for testing ---

    @pytest.fixture
    def birdA(self):
        return Bird('Percy', 3, False, 'Pelican', 1.5, False)

    @pytest.fixture
    def birdB(self):
        return Bird('Evil', 1, True, 'Ostrich', 3.2, True)

    # --- Testing invalid instantiation ---

    def test_instantiation_with_invalid_arguments(self):
        with pytest.raises(ValueError):
            # Invalid name, age, is_female, species name, wingspan, is_flightless, and missing argument
            Bird('E', 1, True, 'Ostrich', 3.2, True)
            Bird('Evil', 0.5, True, 'Ostrich', 3.2, True)
            Bird('Evil', 1, 'yes', 'Ostrich', 3.2, True)
            Bird('Evil', 1, True, 'Astrich', 3.2, True)
            Bird('Evil', 1, True, 'Ostrich', 3, True)
            Bird('Evil', 1, True, 'Ostrich', 3.2, 'yes')
            Bird('Evil', 1, True, 'Ostrich', 3.2)

    # --- Testing getters ---

    def test_get_wingspan(self, birdA, birdB):
        assert birdA.wingspan == 1.5
        assert birdB.wingspan == 3.2

    def test_get_is_flightless(self, birdA, birdB):
        assert birdA.is_flightless is False
        assert birdB.is_flightless is True

    # --- Testing setters ---

    def test_set_wingspan(self, birdA, birdB):
        """Wingspan setter should accept only a float between 0.03 and 3.70."""
        birdA.wingspan = 0.03  # Edge case, 0.03 min
        assert birdA.wingspan == 0.03  # Valid wingspan change
        birdB.wingspan = 3.7  # Edge case, 3.7 max
        assert birdB.wingspan == 3.7  # Valid wingspan change
        birdB.wingspan = 2.0  # Supplied as a float
        assert birdB.wingspan == 2.0  # Valid wingspan change
        with pytest.raises(ValueError):
            birdA.wingspan = 0.02999  # Invalid input, below min value (edge)
            birdA.wingspan = 3.70001  # Invalid input, above max value (edge)
            birdA.wingspan = -0.05  # Invalid input, negative value
            birdB.wingspan = 'big'  # Invalid input, not a float
            birdB.wingspan = 2  # Invalid input, not a float

    def test_set_is_flightless(self, birdA, birdB):
        """Is flightless setter should accept only true and false."""
        birdA.is_flightless = True  # Valid input
        assert birdA.is_flightless is True  # Valid status change
        birdB.is_flightless = False  # Valid input
        assert birdB.is_flightless is False  # Valid status change
        with pytest.raises(ValueError):
            birdA.is_flightless = 'Yes'  # Invalid input, not bool value
            birdB.is_flightless = 1  # Invalid input, not bool value

    # --- Testing behavioural methods ---

    def test_make_sound(self, birdA):
        s = str(birdA.make_sound())
        assert 'Percy' in s
        assert 'Pelican' in s
        assert 'bird call' in s

    def test_eat(self, birdA):
        s = str(birdA.eat())
        assert 'Percy' in s
        assert 'Pelican' in s
        assert 'pecks' in s
        assert 'fish' in s

    def test_sleep(self, birdA):
        s = str(birdA.sleep())
        assert 'Percy' in s
        assert 'Pelican' in s
        assert 'roosts' in s

    def test_move(self, birdA, birdB):
        s = str(birdA.move())
        assert 'Percy' in s
        assert 'Pelican' in s
        assert 'flies' in s
        assert 'aquatic' in s
        s2 = str(birdB.move())
        assert 'walks' in s2

    def test_string_display(self, birdA, birdB):
        s = str(birdA)
        assert 'PERCY' in s
        assert '3' in s
        assert 'Pelican' in s
        assert 'Male' in s
        assert 'fish' in s
        assert 'Aquatic' in s
        assert 'native' in s
        assert '1.5m' in s
        assert 'can fly' in s
        s2 = str(birdB)
        assert 'Female' in s2
        assert 'flightless' in s2
