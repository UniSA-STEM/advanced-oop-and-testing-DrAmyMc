"""
File: main.py
Description: Demonstration class for Zoo Management System.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from mammal import Mammal
from bird import Bird
from reptile import Reptile
from enclosure import Enclosure
from veterinarian import Veterinarian
from zookeeper import Zookeeper
from zoo import Zoo


def demo_create_animal():
    print("\n=== TEST: Creation of Animals ===\n")

    # --- Create and display valid animals ---
    cat = Mammal("Paddy", 3, False, "Lion", "Shaggy")
    pelican = Bird("Percival", 2, True,"Pelican", 2.1, False)
    lizard = Reptile("Lizzie", 1, False,"Lace Monitor", 18, False)
    print(cat)
    print(pelican)
    print(lizard)


def demo_create_enclosure():
    print("\n=== TEST: Creation of Enclosure ===\n")

    # --- Create and display valid enclosure ---
    enc = Enclosure("Reptile House", "Terrarium", 20)
    print(enc)

def demo_add_animals():
    print("\n=== TEST: Adding Animal to Enclosure ===\n")

    # --- Create and display valid enclosure and animals ---
    enc = Enclosure("Test Enclosure", "Aquatic", 30)
    print(enc)
    person = Veterinarian("Test Vet", 2025)
    bird1 = Bird("Percy1", 2, "Pelican")
    bird2 = Bird("Percy2", 2, "Pelican")
    bird3 = Bird("Percy3", 2, "Pelican")
    bird4 = Bird("Percy4", 2, "Pelican")
    cat = Mammal("Puddy", 3, "Lion")
    otter = Mammal("Otty", 1, "Otter")

    # --- Add valid and attempt to add invalid selections to enclosure --
    enc.add_animal(person)      # Not a valid animal object
    enc.add_animal(cat)         # Not an environmental match
    enc.add_animal(bird1)       # Valid addition, sets enclosure to Pelican
    enc.add_animal(otter)       # Not the correct species
    enc.add_animal(bird2)       # Valid addition
    enc.add_animal(bird3)       # Valid addition
    enc.add_animal(bird4)       # No more space in enclosure
    print(enc)                  # Enclosure will now contain 3 pelicans

def demo_check_capacity_list_animals():
    print("\n=== TEST: Checking Enclosure Capacity and Animal Listing ===\n")

    # --- Create and display empty enclosure ---
    enc = Enclosure("Test Enclosure", "Aquatic", 30)
    print(enc)
    enc.list_animals()
    enc.check_capacity()

    # --- Create test animals ---
    bird1 = Bird("Percy1", 2, "Pelican")
    bird2 = Bird("Percy2", 2, "Pelican")
    bird3 = Bird("Percy3", 2, "Pelican")

    # --- Add animals, list animals and check capacity ---
    enc.add_animal(bird1)
    enc.list_animals()
    enc.check_capacity()
    enc.add_animal(bird2)
    enc.list_animals()
    enc.check_capacity()
    enc.add_animal(bird3)
    enc.list_animals()
    enc.check_capacity()

def demo_create_staff():
    """
    Direct tests for the Staff superclass and subclasses for staff creation, setting attributes
    and string display.

    Tests:
        - Creation of staff instances (valid and invalid cases).
        - Setting attributes manually (valid and invalid cases).
        - Displaying string representations.
    """
    print("\n=== TEST: Creation of Staff ===\n")

    # --- Create and display valid staff ---
    vet = Veterinarian("Joe Boggs", 2025)
    zookeeper = Zookeeper("Sally Fubbs", 2025)
    print(vet)
    print(zookeeper)

  # --- Attempt to create staff with invalid name ---
    vet2 = Veterinarian("John", 2025)
    print(vet2)

    # --- Modify staff attributes to valid values ---
    vet.name = "Jimmy Giggle"
    zookeeper.name = "Hoot McHoot"
    vet.year_hired = 2010
    zookeeper.year_hired = 2050
    print(vet)
    print(zookeeper)

    # --- Attempt to modify staff attributes to invalid values ---
    vet.name = "Jim"
    zookeeper.name = "Hoot"
    vet.year_hired = 2009
    zookeeper.year_hired = 2051
    print(vet)
    print(zookeeper)

def demo_create_health_record():
    """
    Direct tests for the HealthRecord class for creation of health records.

    Tests:
        - Creation of a Health Record instance (valid and invalid case).
        - Setting attributes manually (valid and invalid cases).
        - Displaying string representations.
    """
    print("\n=== TEST: Creation of Health Record ===\n")

    # --- Create and display valid health record ---
    record = HealthRecord("Injury", 3, "12 Nov 2025",
                          "Laceration on left front leg", "Clean and bandage wound and monitor.")
    print(record)

    # --- Attempt to create health record with invalid type ---
    record2 = HealthRecord("Leg", 3, "12 Nov 2025",
                          "Laceration on left front leg", "Clean and bandage wound and monitor.")
    print(record2)

    # --- Modify health record attributes to valid values ---
    record.issue_type = 'Illness'
    record.severity_level = 0
    record.date_reported = "10 Nov 2025"
    record.description = "Lethargic due to minor fever"
    record.is_current = False
    record.treatment_plan = "Monitor, but no other changes necessary."
    print(record)

    # --- Attempt to modify health record attributes to invalid values ---
    record.issue_type = 'Leg'
    record.severity_level = -1
    record.severity_level = 4
    record.severity_level = "bad"
    record.date_reported = "10th"
    record.description = "Bad"
    record.is_current = "yes"
    record.treatment_plan = "None"
    print(record)

def demo_update_health_record():
    """
    Direct tests for the HealthRecord class for updating health records.

    Tests:
        - Updating health record (valid and invalid cases).
        - Displaying string representations.
    """
    print("\n=== TEST: Updating of Health Record ===\n")

    # --- Create and display valid health record ---
    record = HealthRecord("Injury", 3, "12 Nov 2025",
                          "Laceration on left front leg", "Clean and bandage wound and monitor.")
    print(record)

    # --- Add treatment plan notes then resolve issue ---
    record.update_treatment_plan("Change dressing twice daily.")            #Valid
    record.update_treatment_plan("Continue to monitor for two more days.")  #Valid
    record.update_treatment_plan("Ok")                                      #Invalid output, length insufficient
    record.issue_resolved()
    print(record)

def demo_add_health_record():
    """
    Tests creation of health records for an animal.

    Tests:
        - Creation of a Health Record instance for a specific animal.
    """
    print("\n=== TEST: Add Health Record to Animal ===\n")

    # --- Create animal ---
    cat = Mammal("Paddy", 3, "Lion", False)
    print(cat)

    # --- Create and display valid health record ---
    cat.add_health_record("Injury", 3, "12 Nov 2025",
                          "Laceration on left front leg", "Clean and bandage wound and monitor.")

def demo_create_zoo():
    """
    Direct tests for the Zoo class for zoo creation, setting attributes and string display.

    Tests:
        - Creation of a zoo instance (valid and invalid case).
        - Setting name manually (valid and invalid cases).
        - Displaying string representations.
    """
    print("\n=== TEST: Creation of Zoo ===\n")

    # --- Create and display valid zoo ---
    zoo = Zoo("Halls Gap Zoo")
    print(zoo)

    # --- Attempt to create zoo with invalid name ---
    zoo2 = Zoo(123)
    print(zoo2)

    # --- Modify zoo name ---
    zoo.name = 'Grampians Zoo'  # Valid name
    zoo.name = 1234             # Invalid name (not a string)
    zoo.name = ''               # Invalid name (empty string)
    print(zoo)

def demo_add_enclosure():
    zoo = Zoo("Halls Gap Zoo")
    zoo.add_enclosure("Reptile House", "Terrarium", 20)
    print(zoo)

# def main():
    """Calls all the demo functions"""

    # --- Demonstrating animal class ---
    # demo_create_animal()

    # --- Demonstrating enclosure class ---
    #demo_create_enclosure()
    #demo_report_status()
    #demo_add_animals()
    #demo_check_capacity_list_animals()

    # --- Demonstrating staff class ---
    #demo_create_staff()

    # --- Demonstrating health record class ---
    #demo_create_health_record()
    #demo_update_health_record()
    #demo_add_health_record()

    # --- Demonstrating zoo class ---
    #demo_create_zoo()
    #demo_add_enclosure()

# GIANT SIM SCRIPT
def main():
    zoo = Zoo("Halls Gap Zoo")
    vet = Veterinarian(123456, 'Mick', 'Rooney', '20/11/2025')
    zookeeper = Zookeeper(123457, 'Nick', 'Mooney', '18/11/2025')
    encA = Enclosure('Penguin Land', 'Aquatic', 100)
    encB = Enclosure('African Plains', 'Savannah', 1000)
    birdA = Bird('Percy', 3, False, 'Pelican', 1.5, False)
    birdB = Bird('Evil', 1, True, 'Ostrich', 3.2, True)
    reptileA = Reptile("Lizzie", 1, False, "Lace Monitor", 18, False)
    reptileB = Reptile('Hissy', 3, True, 'Brown Snake', 21, True)
    mammalA = Mammal('Paddy', 3, False, 'Lion', 'Shaggy')
    mammalB = Mammal('Blinky', 1, True, 'Koala', 'Short')
    print(zoo)
    zoo.add_staff(vet)
    zoo.add_staff(zookeeper)
    zoo.add_enclosure(encA)
    zoo.add_enclosure(encB)
    zoo.add_animal(birdA)
    zoo.add_animal(reptileA)
    zoo.add_animal(mammalA)
    zoo.add_animal(birdB)
    zoo.add_animal(reptileB)
    zoo.add_animal(mammalB)
    print(zoo)
    zoo.remove_staff(123457)
    zoo.remove_enclosure('Penguin Land')
    zoo.remove_animal('Hissy', 'Brown Snake')
    print(zoo)
    zoo.assign_animal('Paddy', 'Lion', 'African Plains')


# Call main function to run tests
if __name__ == "__main__":
    main()
