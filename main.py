"""
File: main.py
Description: Demonstration class for Zoo Management System.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Veterinarian, Zookeeper
from zoo import Zoo
from enclosure import Enclosure
from animal import Mammal, Bird, Reptile


def test_create_animal():
    """
        Direct tests for the Animal superclass and subclasses for animal creation, setting attributes
        and string display.

        Tests:
            - Creation of animal instances (valid and invalid cases).
            - Setting attributes manually (valid and invalid cases).
            - Displaying string representations.
        """
    print("\n=== TEST: Creation of Animals ===\n")

    # --- Create and display valid animals ---
    cat = Mammal("Paddy", 3, "Lion")
    pelican = Bird("Percival", 2, "Pelican")
    lizard = Reptile("Lizzie", 1, "Lace Monitor")
    print(cat)
    print(pelican)
    print(lizard)

    # --- Attempt to create animals with invalid species ---
    cat2 = Mammal("Paddy", 3, "llion")
    print(cat2)

    # --- Modify animal attributes to valid values ---
    cat.name = "Puddy"
    cat.age = 0
    cat.species = "tiger"       # Will automatically convert to title case when matching
    print(cat)

    # --- Attempt to modify animal attributes to invalid values ---
    cat.name = "P"
    cat.age = -1
    cat.age = 201
    cat.age = "old"
    cat.species = "llion"
    print(cat)

def test_create_enclosure():
    """
    Direct tests for the Enclosure class for enclosure creation, setting attributes and string display.

    Tests:
        - Creation of an enclosure instance (valid and invalid case).
        - Setting attributes manually (valid and invalid cases).
        - Displaying string representations.
    """
    print("\n=== TEST: Creation of Enclosure ===\n")

    # --- Create and display valid enclosure ---
    enc = Enclosure("Reptile House", "Terrarium", 20)
    print(enc)

    # --- Attempt to create enclosure with invalid name ---
    enc2 = Enclosure(123, "Terrarium", 20)
    print(enc2)

    # --- Modify enclosure attributes to valid values ---
    enc.name = 'Koala Land'
    enc.type = 'Bushland'
    enc.size = 5000
    enc.cleanliness_level = 0
    enc.animal_type = 'koala'   # Will automatically convert to title case when matching
    print(enc)

    # --- Attempt to modify enclosure attributes to invalid values ---
    enc.name = 'Ba'
    enc.type = 'Bush'
    enc.size = 0
    enc.size = 5001
    enc.size = 'big'
    enc.cleanliness_level = -1
    enc.cleanliness_level = 6
    enc.cleanliness_level = 'dirty'
    enc.animal_type = 'Koalaass'
    print(enc)

def test_add_animal():
    """
    Direct tests for the Enclosure class for adding animal to enclosure.

    Tests:
        - Creation of an enclosure instance (valid and invalid case).
        - Setting attributes manually (valid and invalid cases).
        - Displaying string representations.
    """
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
    enc.add_animal(person)      # Not a valid animal object
    enc.add_animal(cat)
    enc.add_animal(bird1)
    enc.add_animal(otter)
    enc.add_animal(bird2)
    enc.add_animal(bird3)
    enc.add_animal(bird4)
    print(enc)
    print(enc.animals_housed)

def test_create_staff():
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

def test_create_zoo():
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

def test_add_enclosure():
    zoo = Zoo("Halls Gap Zoo")
    zoo.add_enclosure("Reptile House", "Terrarium", 20)
    print(zoo)

def main():
    """Calls all the test functions"""

    # --- Testing animal class ---
    #test_create_animal()

    # --- Testing enclosure class ---
    #test_create_enclosure()
    test_add_animal()

    # --- Testing staff class ---
    #test_create_staff()

    # --- Testing zoo class ---
    #test_create_zoo()
    #test_add_enclosure()

# Call main function to run tests
if __name__ == "__main__":
    main()
