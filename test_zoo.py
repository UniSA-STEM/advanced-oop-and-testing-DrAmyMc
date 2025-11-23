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

    @pytest.fixture
    def encD(self):
        return Enclosure('Small Plains', 'Savannah', 500)

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

    # --- Zoo instance for testing ---

    @pytest.fixture
    def zooA(self):
        return Zoo('Halls Gap Zoo')

    @pytest.fixture
    def zooB(self, mammalA, mammalB, birdA, birdB, reptileA, reptileB, encA, encB, encC, encD,
             vetA, vetB, keeperA, keeperB):
        zoo = Zoo('Grampians Zoo')
        zoo.add_animal(mammalA)
        zoo.add_animal(mammalB)
        zoo.add_animal(birdA)
        zoo.add_animal(birdB)
        zoo.add_animal(reptileA)
        zoo.add_animal(reptileB)
        zoo.add_enclosure(encA)
        zoo.add_enclosure(encB)
        zoo.add_enclosure(encC)
        zoo.add_enclosure(encD)
        zoo.add_staff(vetA)
        zoo.add_staff(vetB)
        zoo.add_staff(keeperA)
        zoo.add_staff(keeperB)
        zoo.assign_enclosure_to_staff('Reptile House', 123456)
        zoo.assign_enclosure_to_staff('Pelican Palace', 123457)
        zoo.assign_enclosure_to_staff('Reptile House', 123458)
        zoo.assign_enclosure_to_staff('Pelican Palace', 123459)
        zoo.assign_animal_to_enclosure('Paddy', 'Lion', 'Small Plains')
        return zoo

    # --- Testing invalid instantiation ---

    def test_instantiation_with_missing_argument(self):
        with pytest.raises(TypeError):
            Zoo()

    def test_instantiation_with_invalid_staffid(self):
        with pytest.raises(ValueError):
            Zoo('X')

    # --- Testing getters ---

    def test_get_name(self, zooA, zooB):
        assert zooA.name == 'Halls Gap Zoo'
        assert zooB.name == 'Grampians Zoo'

    def test_get_animals(self, zooA, zooB, mammalA, mammalB, birdA, birdB, reptileA, reptileB):
        assert zooA.animals == set()
        assert zooB.animals == set([mammalA, mammalB, birdA, birdB, reptileA, reptileB])

    def test_get_enclosures(self, zooA, zooB, encA, encB, encC, encD):
        assert zooA.enclosures == set()
        assert zooB.enclosures == set([encA, encB, encC, encD])

    def test_get_staff(self, zooA, zooB, vetA, vetB, keeperA, keeperB):
        assert zooA.staff == set()
        assert zooB.staff == set([vetA, vetB, keeperA, keeperB])

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

    # --- Testing helper methods ---

    def test_lookup_animal_exists(self, zooB, mammalA, reptileB):
        assert zooB.lookup_animal('Paddy', 'Lion') is mammalA
        assert zooB.lookup_animal('Hissy', 'Brown Snake') is reptileB

    def test_lookup_animal_not_exists(self, zooB):
        assert zooB.lookup_animal('Puddy', 'Lion') is None
        assert zooB.lookup_animal('Hissy', 'Snake') is None

    def test_lookup_enclosure_exists(self, zooB, encA, encB):
        assert zooB.lookup_enclosure('Reptile House') is encA
        assert zooB.lookup_enclosure('Pelican Palace') is encB

    def test_lookup_enclosure_not_exists(self, zooB):
        assert zooB.lookup_enclosure('Reptile Palace') is None
        assert zooB.lookup_enclosure('Pelican House') is None

    def test_lookup_staff_exists(self, zooB, vetA, keeperA):
        assert zooB.lookup_staff(123456) is vetA
        assert zooB.lookup_staff(123458) is keeperA

    def test_lookup_staff_not_exists(self, zooB):
        assert zooB.lookup_staff(223456) is None
        assert zooB.lookup_staff(223458) is None

    # --- Testing add/remove animals/enclosures/staff behavioural methods ---

    def test_add_animal_valid(self, zooA, mammalA, birdA, reptileA):
        assert zooA.add_animal(mammalA) == 'Paddy the Lion added to the zoo.'
        assert zooA.add_animal(birdA) == 'Percy the Pelican added to the zoo.'
        assert zooA.add_animal(reptileA) == 'Lizzie the Lace Monitor added to the zoo.'
        assert len(zooA.animals) == 3
        assert zooA.animals == set([mammalA, birdA, reptileA])

    def test_add_animal_invalid_object(self, zooA, encA):
        with pytest.raises(TypeError):
            zooA.add_animal(encA)

    def test_add_enclosure_valid(self, zooA, encA, encB, encC):
        assert zooA.add_enclosure(encA) == 'Reptile House enclosure added to the zoo.'
        assert zooA.add_enclosure(encB) == 'Pelican Palace enclosure added to the zoo.'
        assert zooA.add_enclosure(encC) == 'African Plains enclosure added to the zoo.'
        assert len(zooA.enclosures) == 3
        assert zooA.enclosures == set([encA, encB, encC])

    def test_add_enclosure_invalid_object(self, zooA, mammalA):
        with pytest.raises(TypeError):
            zooA.add_enclosure(mammalA)

    def test_add_staff_valid(self, zooA, vetA, keeperA):
        assert zooA.add_staff(vetA) == 'Veterinarian Zoe Smith added to the zoo.'
        assert zooA.add_staff(keeperA) == 'Zookeeper Joe Blogg added to the zoo.'
        assert len(zooA.staff) == 2
        assert zooA.staff == set([keeperA, vetA])

    def test_add_staff_invalid_object(self, zooA, encA):
        with pytest.raises(TypeError):
            zooA.add_staff(encA)

    def test_remove_animal_valid(self, zooB, mammalA, encD):
        assert len(zooB.animals) == 6
        assert mammalA in zooB.animals
        assert mammalA in encD.animals_housed
        assert zooB.remove_animal('Paddy', 'Lion') == 'Paddy the Lion removed from the zoo.'
        assert len(zooB.animals) == 5
        assert mammalA not in zooB.animals
        assert mammalA not in encD.animals_housed

    def test_remove_animal_not_found(self, zooB):
        with pytest.raises(ValueError):
            zooB.remove_animal('Puddy', 'Lion')

    def test_remove_enclosure_valid(self, zooB, encB, vetB, keeperB):
        assert len(zooB.enclosures) == 4
        assert encB in zooB.enclosures
        assert encB in vetB.assigned_enclosures
        assert encB in keeperB.assigned_enclosures
        assert zooB.remove_enclosure('Pelican Palace') == 'Pelican Palace enclosure removed from the zoo.'
        assert len(zooB.enclosures) == 3
        assert encB not in zooB.enclosures
        assert encB not in vetB.assigned_enclosures
        assert encB not in keeperB.assigned_enclosures

    def test_remove_enclosure_not_found(self, zooB):
        with pytest.raises(ValueError):
            zooB.remove_enclosure('Pelican Place')

    def test_remove_staff_valid(self, zooB, vetA, encA):
        assert len(zooB.staff) == 4
        assert vetA in zooB.staff
        assert encA.assigned_vet == vetA
        assert zooB.remove_staff(123456) == 'Veterinarian Zoe Smith removed from the zoo.'
        assert len(zooB.staff) == 3
        assert vetA not in zooB.staff
        assert encA.assigned_vet is None

    def test_remove_staff_not_found(self, zooB):
        with pytest.raises(ValueError):
            zooB.remove_staff(223456)

    # --- Testing assignment of animals/staff behavioural methods ---

    def test_assign_enclosure_to_staff_invalid_animal(self, zooB):
        with pytest.raises(ValueError):
            zooB.assign_animal_to_enclosure('Puddy', 'Lion', 'African Plains')

    def test_assign_animal_to_enclosure_invalid_enclosure(self, zooB):
        with pytest.raises(ValueError):
            zooB.assign_animal_to_enclosure('Paddy', 'Lion', 'Africa')

    def test_assign_animal_to_enclosure_invalid_animal_under_treatment(self, zooB, mammalA, encC):
         mammalA.on_display = False
         with pytest.raises(ValueError):
             zooB.assign_animal_to_enclosure('Paddy', 'Lion', 'African Plains')

    def test_assign_animal_to_enclosure_valid(self, zooB, mammalA, encC, encD):
        assert encC.animals_housed == []
        assert encD.animals_housed == [mammalA]
        msg = zooB.assign_animal_to_enclosure('Paddy', 'Lion', 'African Plains')
        assert msg == 'Paddy the Lion is now assigned to the African Plains enclosure.'
        assert encC.animals_housed == [mammalA]
        assert encD.animals_housed == []

    def test_assign_enclosure_to_staff_invalid_enclosure(self, zooB):
        with pytest.raises(ValueError):
            zooB.assign_enclosure_to_staff('Pelican Place', 123456)

    def test_assign_enclosure_to_staff_invalid_staff(self, zooB):
        with pytest.raises(ValueError):
            zooB.assign_enclosure_to_staff('Pelican Palace', 223456)

    def test_assign_enclosure_to_staff_valid_vet(self, zooB, encA, encB, vetA, vetB):
        assert encB.assigned_vet == vetB
        assert vetA.assigned_enclosures == [encA]
        assert vetB.assigned_enclosures == [encB]
        msg = zooB.assign_enclosure_to_staff('Pelican Palace', 123456)
        assert msg == 'Zoe Smith is now the assigned Veterinarian for the Pelican Palace enclosure.'
        assert encB.assigned_vet == vetA
        assert vetA.assigned_enclosures == [encA, encB]
        assert vetB.assigned_enclosures == []

    def test_assign_enclosure_to_staff_valid_keeper(self, zooB, encA, encB, keeperA, keeperB):
        assert encB.assigned_keeper == keeperB
        assert keeperA.assigned_enclosures == [encA]
        assert keeperB.assigned_enclosures == [encB]
        msg = zooB.assign_enclosure_to_staff('Pelican Palace', 123458)
        assert msg == 'Joe Blogg is now the assigned Zookeeper for the Pelican Palace enclosure.'
        assert encB.assigned_keeper == keeperA
        assert keeperA.assigned_enclosures == [encA, encB]
        assert keeperB.assigned_enclosures == []
