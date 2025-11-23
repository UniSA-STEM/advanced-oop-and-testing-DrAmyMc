"""
File: test_zoo.py
Description: Testing suite for the Zoo class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest

from zoo import Zoo
from enclosure import Enclosure
from mammal import Mammal
from bird import Bird
from reptile import Reptile
from veterinarian import Veterinarian
from zookeeper import Zookeeper
from healthrecord import HealthRecord


class TestZoo:
    """Testing suite for the Zoo class."""

    # --- Animal instances for testing ---

    @pytest.fixture
    def mammalA(self):
        return Mammal('Paddy', 3, False, 'Lion', 'Shaggy')

    @pytest.fixture
    def mammalB(self):
        return Mammal('Fluffy', 1, True, 'Lion', 'Short')

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

    # --- Health Record instances for testing ---

    @pytest.fixture
    def recA(self, vetA):
        return HealthRecord(0, 2, '12/11/2025', 'Laceration',
                            'Clean and bandage.', vetA)

    @pytest.fixture
    def recB(self, vetA):
        return HealthRecord(2, 1, '8/9/2024', 'Lethargy',
                            'Monitor for fever.', vetA)

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
        zoo.assign_enclosure_to_staff('Reptile House', 123458)
        zoo.assign_enclosure_to_staff('Pelican Palace', 123457)
        zoo.assign_enclosure_to_staff('Pelican Palace', 123459)
        zoo.assign_enclosure_to_staff('African Plains', 123456)
        zoo.assign_enclosure_to_staff('African Plains', 123458)
        zoo.assign_enclosure_to_staff('Small Plains', 123457)
        zoo.assign_enclosure_to_staff('Small Plains', 123459)
        zoo.assign_animal_to_enclosure('Paddy', 'Lion', 'Small Plains')
        zoo.assign_animal_to_enclosure('Fluffy', 'Lion', 'Small Plains')
        zoo.assign_animal_to_enclosure('Lizzie', 'Lace Monitor', 'Reptile House')
        zoo.assign_animal_to_enclosure('Percy', 'Pelican', 'Pelican Palace')
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

    def test_assign_animal_to_enclosure_valid(self, zooB, mammalA, mammalB, encC, encD):
        assert encC.animals_housed == []
        assert encD.animals_housed == [mammalA, mammalB]
        msg = zooB.assign_animal_to_enclosure('Paddy', 'Lion', 'African Plains')
        assert msg == 'Paddy the Lion is now assigned to the African Plains enclosure.'
        assert encC.animals_housed == [mammalA]
        assert encD.animals_housed == [mammalB]

    def test_assign_enclosure_to_staff_invalid_enclosure(self, zooB):
        with pytest.raises(ValueError):
            zooB.assign_enclosure_to_staff('Pelican Place', 123456)

    def test_assign_enclosure_to_staff_invalid_staff(self, zooB):
        with pytest.raises(ValueError):
            zooB.assign_enclosure_to_staff('Pelican Palace', 223456)

    def test_assign_enclosure_to_staff_valid_vet(self, zooB, encA, encB, encC, encD, vetA, vetB):
        assert encB.assigned_vet == vetB
        assert vetA.assigned_enclosures == [encA, encC]
        assert vetB.assigned_enclosures == [encB, encD]
        msg = zooB.assign_enclosure_to_staff('Pelican Palace', 123456)
        assert msg == 'Zoe Smith is now the assigned Veterinarian for the Pelican Palace enclosure.'
        assert encB.assigned_vet == vetA
        assert vetA.assigned_enclosures == [encA, encC, encB]
        assert vetB.assigned_enclosures == [encD]

    def test_assign_enclosure_to_staff_valid_keeper(self, zooB, encA, encB, encC, encD, keeperA, keeperB):
        assert encB.assigned_keeper == keeperB
        assert keeperA.assigned_enclosures == [encA, encC]
        assert keeperB.assigned_enclosures == [encB, encD]
        msg = zooB.assign_enclosure_to_staff('Pelican Palace', 123458)
        assert msg == 'Joe Blogg is now the assigned Zookeeper for the Pelican Palace enclosure.'
        assert encB.assigned_keeper == keeperA
        assert keeperA.assigned_enclosures == [encA, encC, encB]
        assert keeperB.assigned_enclosures == [encD]

    # --- Testing scheduling behavioural methods ---

    def test_schedule_feeding(self, zooB):
        s = zooB.schedule_feeding()
        assert 'FEEDING TIME AT GRAMPIANS ZOO' in s
        assert 'Joe Blogg fed insects to the Lace Monitors in Reptile House.'
        assert 'Jim Doe fed fish to the Pelicans in Pelican Palace.'
        assert 'Cannot feed animals in African Plains. This enclosure is empty.' in s
        assert 'Jim Doe fed meat to the Lions in Small Plains.'

    def test_schedule_cleaning(self, zooB, encA, encB):
        encA.cleanliness_level = 3
        encB.cleanliness_level = 3
        s = zooB.schedule_cleaning()
        assert 'CLEANING TIME AT GRAMPIANS ZOO' in s
        assert 'Joe Blogg cleaned the Reptile House enclosure.'
        assert 'Jim Doe cleaned the Pelican Palace enclosure.'
        assert 'Cannot clean African Plains. This enclosure is already pristine.' in s
        assert 'Cannot clean Small Plains. This enclosure is already pristine.' in s

    def test_schedule_health_checks(self, zooB):
        s = zooB.schedule_health_checks()
        assert 'HEALTH CHECK TIME AT GRAMPIANS ZOO' in s
        assert 'Zoe Smith conducted health checks on the Lace Monitors in Reptile House.'
        assert 'Sally Brown conducted health checks on the Pelicans in Pelican Palace.'
        assert 'Cannot conduct health checks in African Plains. This enclosure is empty.' in s
        assert 'Sally Brown conducted health checks on the Lions in Small Plains.'

    # --- Testing reporting behavioural methods ---

    def test_list_animal_health_history_animal_not_found(self, zooB):
        with pytest.raises(ValueError):
            zooB.list_animal_health_history('Puddy', 'Lion')

    def test_list_animal_health_history_no_records(self, zooB):
        s = zooB.list_animal_health_history('Paddy', 'Lion')
        assert 'HEALTH HISTORY FOR PADDY THE LION' in s
        assert 'No health records found.' in s

    def test_list_animal_health_history(self, zooB, reptileA, recA, recB):
        reptileA.add_health_record(recA)
        reptileA.add_health_record(recB)
        s = zooB.list_animal_health_history('Lizzie', 'Lace Monitor')
        assert 'HEALTH HISTORY FOR LIZZIE THE LACE MONITOR' in s
        assert 'Laceration' in s
        assert 'Lethargy' in s

    def test_list_animals_under_treatment_none_unwell(self, zooB):
        s = zooB.list_animals_under_treatment()
        assert 'ANIMALS CURRENTLY UNDER TREATMENT' in s
        assert 'No current health records found.' in s

    def test_list_animals_under_treatment(self, zooB, reptileA, birdA, mammalA, recA, recB):
        reptileA.add_health_record(recA)
        birdA.add_health_record(recB)
        mammalA.add_health_record(recA)
        s = zooB.list_animals_under_treatment()
        assert 'ANIMALS CURRENTLY UNDER TREATMENT' in s
        assert 'No current health records found.' not in s
        assert 'Paddy, Lion, Male, aged 3 years, Moderate Injury' in s
        assert 'Percy, Pelican, Male, aged 3 years, Minor Behavioural Issue' in s
        assert 'Lizzie, Lace Monitor, Male, aged 1 years, Moderate Injury' in s

    def test_list_animals_by_species(self, zooB):
        pass

    def test_list_enclosures_by_status(self, zooB):
        pass

    # --- Testing string display ---

    def test_string_display(self, zooA):
        s = str(zooA)
        assert 'HALLS GAP ZOO' in s
        assert 'no animals' in s
        assert 'no enclosures' in s
        assert 'no staff' in s

    def test_string_display_alt_values(self, zooB):
        s = str(zooB)
        assert 'GRAMPIANS ZOO' in s
        assert '6 animals' in s
        assert '4 enclosures' in s
        assert '4 staff' in s