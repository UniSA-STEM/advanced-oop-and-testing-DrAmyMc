"""
File: test_veterinarian.py
Description: Testing suite for the Veterinarian child class.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from veterinarian import Veterinarian
from enclosure import Enclosure
from mammal import Mammal
from healthrecord import HealthRecord


class TestVeterinarian:
    """Testing suite for the Veterinarian class."""

    # --- Enclosure instances for testing interactive behavioural methods ---

    @pytest.fixture
    def encA(self):
        return Enclosure('African Plains', 'Savannah', 2000)

    @pytest.fixture
    def encB(self):
        enc = Enclosure('Penguin Palace', 'Aquatic', 50)
        enc.animal_type = 'Fairy Penguin'
        return enc

    # --- Mammal instances for testing interactive behavioural methods ---

    @pytest.fixture
    def animalA(self):
        return Mammal('Paddy', 3, True, 'Lion', 'Shaggy')

    @pytest.fixture
    def animalB(self):
        animal = Mammal('Puddy', 3, True, 'Lion', 'Shaggy')
        record = HealthRecord(1, 2, '20/11/2025', 'Mild fever',
                              'Monitor', None)
        animal.add_health_record(record)
        return animal

    # --- Veterinarian instance for testing ---

    @pytest.fixture
    def vetA(self, encA, encB):
        vet = Veterinarian(123457, 'Zoe', 'Vlogg', '8/9/2024')
        vet.add_assigned_enclosure(encA)
        vet.add_assigned_enclosure(encB)
        return vet

    # --- Testing getters ---

    def test_get_role(self, vetA):
        assert vetA.role == 'Veterinarian'

    def test_get_responsibilities(self, vetA):
        assert vetA.responsibilities == ['Conduct health checks', 'Treat animals', 'Plan preventative health care']

    def test_get_assigned_enclosures(self, vetA):
        assert len(vetA.assigned_enclosures) == 2

    # --- Testing behavioural methods ---

    def test_conduct_health_checks_enclosure_not_assigned(self, vetA):
        msg = vetA.conduct_health_checks('Penguins')
        assert msg == 'Cannot conduct health checks in Penguins. Not assigned to this enclosure.'

    def test_conduct_health_checks_empty_enclosure(self, vetA):
        msg = vetA.conduct_health_checks('African Plains')
        assert msg == 'Cannot conduct health checks in African Plains. This enclosure is empty.'

    def test_conduct_health_checks_successful_checks(self, vetA):
        msg = vetA.conduct_health_checks('Penguin Palace')
        assert msg == 'Zoe Vlogg conducted health checks on the Fairy Penguins in Penguin Palace.'

    def test_create_health_record(self, vetA, animalA):
        record = vetA.create_health_record(animalA, 1, 2, '20/11/2025', 'Mild fever', 'Monitor')
        assert isinstance(record, HealthRecord)
        assert len(animalA.health_record) == 1
        assert animalA.health_record[0] == record
        assert animalA.on_display is False
        assert record.vet is vetA

    def test_add_treatment_note_no_record(self, vetA, animalA):
        with pytest.raises(ValueError):
            vetA.add_treatment_note(animalA, 'Continue to monitor')

    def test_add_treatment_note_no_current_record(self, vetA, animalB):
        animalB.health_record[0].mark_issue_resolved()
        with pytest.raises(ValueError):
            vetA.add_treatment_note(animalB, 'Continue to monitor')

    def test_add_treatment_note_successful(self, vetA, animalB):
        vetA.add_treatment_note(animalB, 'Continue to monitor')
        assert len(animalB.health_record[0].treatment_plan) == 2
        assert animalB.health_record[0].treatment_plan[1] == 'Continue to monitor'

    def test_mark_issue_resolved_no_record(self, vetA, animalA):
        with pytest.raises(ValueError):
            vetA.mark_issue_resolved(animalA)

    def test_mark_issue_resolved_no_current_record(self, vetA, animalB):
        animalB.health_record[0].mark_issue_resolved()
        with pytest.raises(ValueError):
            vetA.mark_issue_resolved(animalB)

    def test_mark_issue_resolved_successful(self, vetA, animalB):
        vetA.mark_issue_resolved(animalB)
        assert animalB.health_record[0].is_current is False

    # --- Testing string display ---

    def test_string_display(self, vetA):
        s = str(vetA)
        assert 'VETERINARIAN' in s
        assert 'Responsibilities' in s
        assert 'Conduct health checks' in s
        assert 'Treat animals' in s
        assert 'Plan preventative health care' in s
        assert 'Assigned Enclosures' in s