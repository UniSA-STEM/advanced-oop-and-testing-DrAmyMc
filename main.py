"""
File: main.py
Description: Demonstration class for Zoo Management System.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""
from json.encoder import encode_basestring

from mammal import Mammal
from bird import Bird
from reptile import Reptile
from enclosure import Enclosure
from healthrecord import HealthRecord
from veterinarian import Veterinarian
from zookeeper import Zookeeper
from zoo import Zoo


def main():

    # --- Create instances of animals and display their information ---
    mammalA = Mammal('Paddy', 3, False, 'Lion', 'Shaggy')
    mammalB = Mammal('Fluffy', 1, True, 'Lion', 'Short')
    birdA = Bird('Percy', 3, False, 'Pelican', 1.5, False)
    birdB = Bird('Evil', 1, True, 'Ostrich', 3.2, True)
    reptileA = Reptile("Lizzie", 1, False, "Lace Monitor", 18, False)
    reptileB = Reptile('Hissy', 3, True, 'Brown Snake', 21, True)
    print(mammalA)
    print(mammalB)
    print(birdA)
    print(birdB)
    print(reptileA)
    print(reptileB)

    # --- Demonstrate animal behavioural methods ---
    print('---The animals are making sounds---')
    print(mammalA.make_sound())
    print(mammalB.make_sound())
    print(birdA.make_sound())
    print(birdB.make_sound())
    print(reptileA.make_sound())
    print(reptileB.make_sound())
    print('\n---The animals are eating---')
    print(mammalA.eat())
    print(mammalB.eat())
    print(birdA.eat())
    print(birdB.eat())
    print(reptileA.eat())
    print(reptileB.eat())
    print('\n---The animals are sleeping---')
    print(mammalA.sleep())
    print(mammalB.sleep())
    print(birdA.sleep())
    print(birdA.sleep())
    print(reptileA.sleep())
    print(reptileB.sleep())
    print('\n---The animals are moving---')
    print(mammalA.move())
    print(mammalB.move())
    print(birdA.move())
    print(birdB.move())
    print(reptileA.move())
    print(reptileB.move())
    print('\n---The birds and reptiles are laying eggs---')
    print(birdA.lay_eggs())
    print(birdB.lay_eggs())
    print(reptileA.lay_eggs())
    print(reptileB.lay_eggs())
    print('\n---The reptiles are basking---')
    print(reptileA.bask())
    print(reptileB.bask())
    print('')

    # --- Create instances of enclosures and display their information ---
    encA = Enclosure('Reptile House', 'Terrarium', 20)
    encB = Enclosure('Pelican Palace', 'Aquatic', 30)
    encC = Enclosure('African Plains', 'Savannah', 2000)
    encD = Enclosure('Small Plains', 'Savannah', 500)
    print(encA)
    print(encB)
    print(encC)
    print(encD)

    # --- Create instances of staff and display their information ---
    vetA = Veterinarian(123456, 'Zoe', 'Smith', '12/11/2025')
    vetB = Veterinarian(123457, 'Sally', 'Brown', '8/9/2024')
    keeperA = Zookeeper(123458, 'Joe', 'Blogg', '12/11/2025')
    keeperB = Zookeeper(123459, 'Jim', 'Doe', '8/9/2024')
    print(vetA)
    print(vetB)
    print(keeperA)
    print(keeperB)

    # --- Create instance of a zoo and display its information ---
    zoo = Zoo('Halls Gap Zoo')
    print(zoo)

    # --- Add animals, enclosures, and staff to zoo, and display zoo information ---
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
    print(zoo)

    # --- Assign enclosures to staff and display staff information---
    zoo.assign_enclosure_to_staff('Reptile House', 123456)
    zoo.assign_enclosure_to_staff('Reptile House', 123458)
    zoo.assign_enclosure_to_staff('Pelican Palace', 123457)
    zoo.assign_enclosure_to_staff('Pelican Palace', 123459)
    zoo.assign_enclosure_to_staff('African Plains', 123456)
    zoo.assign_enclosure_to_staff('African Plains', 123458)
    zoo.assign_enclosure_to_staff('Small Plains', 123457)
    zoo.assign_enclosure_to_staff('Small Plains', 123459)
    print(vetA)
    print(vetB)
    print(keeperA)
    print(keeperB)

    # --- Assign animals to enclosures and display enclosure information---
    zoo.assign_animal_to_enclosure('Paddy', 'Lion', 'Small Plains')
    zoo.assign_animal_to_enclosure('Fluffy', 'Lion', 'Small Plains')
    zoo.assign_animal_to_enclosure('Lizzie', 'Lace Monitor', 'Reptile House')
    zoo.assign_animal_to_enclosure('Percy', 'Pelican', 'Pelican Palace')
    print(encA)
    print(encB)
    print(encC)
    print(encD)

    # --- Demonstrate enclosure behavioural methods ---
    encA.become_poopy()
    encA.become_poopy()
    encA.become_poopy()
    encA.become_poopy()
    encB.become_poopy()
    encB.become_poopy()
    encB.become_poopy()
    encD.become_poopy()
    print('---Enclosure A information---')
    print(encA.report_status())
    print(encA.check_capacity())
    print(encA.list_animals_housed())
    print('---Enclosure B information---')
    print(encB.report_status())
    print(encB.check_capacity())
    print(encB.list_animals_housed())
    print('---Enclosure C information---')
    print(encC.report_status())
    print(encC.check_capacity())
    print(encC.list_animals_housed())
    print('---Enclosure C information---')
    print(encD.report_status())
    print(encD.check_capacity())
    print(encD.list_animals_housed())

    # --- Demonstrate zoo behavioural/staff behavioural methods ---
    print(zoo.schedule_feeding())
    print(zoo.schedule_cleaning())
    print(zoo.schedule_health_checks())

    # --- Demonstrate health record behaviour ---
    print(vetA.create_health_record(mammalA, 0, 2, '12/11/2025', 'Laceration', 'Clean and bandage.'))
    print(vetB.create_health_record(birdA, 2, 1, '8/9/2024', 'Lethargy', 'Monitor for fever.'))
    vetA.add_treatment_note(mammalA, 'Redress wound')
    vetA.add_treatment_note(mammalA, 'Continue to monitor')
    vetA.mark_issue_resolved(mammalA)

def next():
# --- Create instances of health records and display their information ---
    recA = HealthRecord(0, 2, '12/11/2025', 'Laceration', 'Clean and bandage.', vetA)
    recB = HealthRecord(2, 1, '8/9/2024', 'Lethargy', 'Monitor for fever.', vetA)
    print(recA)
    print(recB)

# Call main function to run tests
if __name__ == "__main__":
    main()
