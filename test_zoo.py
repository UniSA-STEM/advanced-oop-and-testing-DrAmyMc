"""
File: test_zoo.py
Description: Testing suite for the Zoo class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest

import zoo
from zoo import Zoo
from enclosure import Enclosure
from mammal import Mammal
from bird import Bird
from reptile import Reptile
from veterinarian import Veterinarian
from zookeeper import Zookeeper


class TestZoo:
    """Testing suite for the Zoo class."""

    # --- Zoo instance for testing ---

    @pytest.fixture
    def zooA(self):
        return Zoo('Halls Gap Zoo')

    # --- Enclosures instances for testing ---

    @pytest.fixture
    def encA(self):
        return Enclosure('Reptile House', 'Terrarium', 20)

    @pytest.fixture
    def encB(self):
        return Enclosure('Pelican Palace', 'Aquatic', 30)

    @pytest.fixture
    def encC(self):
        return Enclosure('African Plains', 'Savannah', 2000)

    # --- Animal instances for testing ---

    @pytest.fixture
    def mammalA(self):
        return Mammal('Paddy', 3, False, 'Lion', 'Shaggy')

    @pytest.fixture
    def mammalB(self):
        return Mammal('Blinky', 1, True, 'Koala', 'Short')

    @pytest.fixture
    def birdA(self):
        return Bird('Percy', 3, False, 'Pelican', 1.5, False)

    @pytest.fixture
    def birdB(self):
        return Bird('Evil', 1, True, 'Ostrich', 3.2, True)

    @pytest.fixture
    def reptileA(self):
        return Reptile("Lizzie", 1, False, "Lace Monitor", 18, False)

    @pytest.fixture
    def reptileB(self):
        return Reptile('Hissy', 3, True, 'Brown Snake', 21, True)

    # --- Staff instances for testing ---

    @pytest.fixture
    def vetA(self):
        return Veterinarian(123456, 'Zoe', 'Smith', '12/11/2025')

    @pytest.fixture
    def vetB(self):
        return Veterinarian(123457, 'Sally', 'Brown', '8/9/2024')

    @pytest.fixture
    def keeperA(self):
        return Zookeeper(123458, 'Joe', 'Blogg', '12/11/2025')

    @pytest.fixture
    def keeperB(self):
        return Zookeeper(123459, 'Jim', 'Doe', '8/9/2024')

    # --- Testing invalid instantiation ---

    def test_instantiation_with_missing_argument(self):
        with pytest.raises(TypeError):
            Zoo()

    def test_instantiation_with_invalid_staffid(self):
        with pytest.raises(ValueError):
            Zoo('X')

    # --- Testing getters ---

    def test_get_name(self, zooA):
        assert zooA.name == 'Halls Gap Zoo'

    def test_get_animals(self, zooA):
        assert zooA.animals == set()

    def test_get_enclosures(self, zooA):
        assert zooA.enclosures == set()

    def test_get_staff(self, zooA):
        assert zooA.staff == set()

    # --- Testing setters ---

    def test_set_name_valid_min_length(self, zooA):
        zooA.name = 'Zoo'
        assert zooA.name == 'Zoo'

    def test_set_name_invalid_short_str(self, zooA):
        with pytest.raises(ValueError):
            zooA.name = 'Zo'

    def test_set_name_invalid_input_type_bool(self, zooA):
        with pytest.raises(ValueError):
            zooA.name = False

    # --- Testing add/remove behavioural methods ---

    def test_add_animal_valid(self, zooA, mammalA, birdA, reptileA):
        zooA.add_animal(mammalA)
        zooA.add_animal(birdA)
        zooA.add_animal(reptileA)
        assert len(zooA.animals) == 3
        assert zooA.animals == set([mammalA, birdA, reptileA])

    def test_add_animal_invalid_object(self, zooA, encA):
        with pytest.raises(TypeError):
            zooA.add_animal(encA)

    def test_remove_animal_valid(self, zooA, mammalA, birdA, reptileA):
        zooA.add_animal(mammalA)
        zooA.add_animal(birdA)
        zooA.add_animal(reptileA)
        zooA.remove_animal('Paddy', 'Lion')
        assert len(zooA.animals) == 2
        assert zooA.animals == set([birdA, reptileA])

    def test_remove_animal_not_found(self, zooA, birdA, reptileA):
        zooA.add_animal(birdA)
        zooA.add_animal(reptileA)
        with pytest.raises(ValueError):
            zooA.remove_animal('Paddy', 'Lion')

    def test_add_enclosure_valid(self, zooA, encA, encB, encC):
        zooA.add_enclosure(encA)
        zooA.add_enclosure(encB)
        zooA.add_enclosure(encC)
        assert len(zooA.enclosures) == 3
        assert zooA.enclosures == set([encA, encB, encC])

    def test_add_enclosure_invalid_object(self, zooA, mammalA):
        with pytest.raises(TypeError):
            zooA.add_enclosure(mammalA)

    def test_remove_enclosure_valid(self, zooA, encA, encB, encC):
        zooA.add_enclosure(encA)
        zooA.add_enclosure(encB)
        zooA.add_enclosure(encC)
        zooA.remove_enclosure('Pelican Palace')
        assert len(zooA.enclosures) == 2
        assert zooA.enclosures == set([encA, encC])

    def test_remove_enclosure_not_found(self, zooA, encA, encC):
        zooA.add_enclosure(encA)
        zooA.add_enclosure(encC)
        with pytest.raises(ValueError):
            zooA.remove_enclosure('Pelican Palace')

    def test_add_staff_valid(self, zooA, vetA, vetB, keeperA, keeperB):
        zooA.add_staff(vetA)
        zooA.add_staff(vetB)
        zooA.add_staff(keeperA)
        zooA.add_staff(keeperB)
        assert len(zooA.staff) == 4
        assert zooA.staff == set([keeperA, keeperB, vetA, vetB])

    def test_add_staff_invalid_object(self, zooA, encA):
        with pytest.raises(TypeError):
            zooA.add_staff(encA)

    def test_remove_staff_valid(self, zooA, vetA, vetB, keeperA):
        zooA.add_staff(vetA)
        zooA.add_staff(vetB)
        zooA.add_staff(keeperA)
        zooA.remove_staff(123456)
        assert len(zooA.staff) == 2
        assert zooA.staff == set([keeperA, vetB])

    def test_remove_staff_not_found(self, zooA, vetB, keeperA):
        zooA.add_staff(vetB)
        zooA.add_staff(keeperA)
        with pytest.raises(ValueError):
            zooA.remove_staff(123456)