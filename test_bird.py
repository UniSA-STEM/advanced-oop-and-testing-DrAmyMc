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

    def test_instantiation_with_missing_argument(self):
        with pytest.raises(TypeError):
            Bird('Evil', 1, True, 'Ostrich', 3.2)

    def test_instantiation_with_invalid_name(self):
        with pytest.raises(ValueError):
            Bird('E', 1, True, 'Ostrich', 3.2, True)

    def test_instantiation_with_invalid_age(self):
        with pytest.raises(ValueError):
            Bird('Evil', 0.5, True, 'Ostrich', 3.2, True)

    def test_instantiation_with_invalid_is_female(self):
        with pytest.raises(ValueError):
            Bird('Evil', 1, 'yes', 'Ostrich', 3.2, True)

    def test_instantiation_with_invalid_species(self):
        with pytest.raises(ValueError):
            Bird('Evil', 1, True, 'Astrich', 3.2, True)

    def test_instantiation_with_invalid_wingspan(self):
        with pytest.raises(ValueError):
            Bird('Evil', 1, True, 'Ostrich', 0, True)

    def test_instantiation_with_invalid_flightless(self):
        with pytest.raises(ValueError):
            Bird('Evil', 1, True, 'Ostrich', 3.2, 'yes')

    # --- Testing getters ---

    def test_get_wingspan(self, birdA, birdB):
        assert birdA.wingspan == 1.5
        assert birdB.wingspan == 3.2

    def test_get_is_flightless(self, birdA, birdB):
        assert birdA.is_flightless is False
        assert birdB.is_flightless is True

    # --- Testing setters ---

    def test_set_wingspan_valid_min_edge(self, birdA):
        birdA.wingspan = 0.03
        assert birdA.wingspan == 0.03

    def test_set_wingspan_valid_max_edge(self, birdA):
        birdA.wingspan = 3.7
        assert birdA.wingspan == 3.7

    def test_set_wingspan_valid_int(self, birdA):
        birdA.wingspan = 2
        assert birdA.wingspan == 2.0

    def test_set_wingspan_invalid_below_min(self, birdA):
        with pytest.raises(ValueError):
            birdA.wingspan = 0.02999

    def test_set_wingspan_invalid_above_max(self, birdA):
        with pytest.raises(ValueError):
            birdA.wingspan = 3.70001

    def test_set_wingspan_invalid_input_type_bool(self, birdA):
        with pytest.raises(ValueError):
            birdA.wingspan = True

    def test_set_is_flightless_valid(self, birdA, birdB):
        birdA.is_flightless = True
        assert birdA.is_flightless is True
        birdB.is_flightless = False
        assert birdB.is_flightless is False

    def test_set_is_flightless_invalid_input_type_int(self, birdA):
        with pytest.raises(ValueError):
            birdA.is_flightless = 1

    # --- Testing behavioural methods ---

    def test_make_sound(self, birdA):
        assert birdA.make_sound() == 'Percy the Pelican makes a bird call.'

    def test_eat(self, birdA):
        assert birdA.eat() == 'Percy the Pelican pecks at their fish.'

    def test_sleep(self, birdA):
        assert birdA.sleep() == 'Percy the Pelican roosts and goes to sleep.'

    def test_move_flying(self, birdA):
        assert birdA.move() == 'Percy the Pelican flies around their aquatic enclosure.'

    def test_move_walking(self, birdB):
        assert birdB.move() == 'Evil the Ostrich walks around their savannah enclosure.'

    def test_lay_eggs_valid_female(self, birdB):
        assert birdB.lay_eggs() == 'Evil the Ostrich lays eggs.'

    def test_lay_eggs_invalid_male(self, birdA):
        assert birdA.lay_eggs() == 'Percy cannot lay eggs because he is male.'

    # --- Testing string display ---

    def test_string_display_flighted(self, birdA):
        s = str(birdA)
        assert 'PERCY' in s
        assert 'BIRD' in s
        assert 'Wingspan' in s
        assert '1.5m' in s
        assert 'This bird can fly' in s

    def test_string_display_flightless(self, birdB):
        s = str(birdB)
        assert '3.2m' in s
        assert 'This bird is flightless' in s
