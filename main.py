"""
File: main.py
Description: Demonstration class for Zoo Management System.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Veterinarian
from staff import Zookeeper
from zoo import Zoo
from enclosure import Enclosure
from animal import Carnivore


def test_create_animal():
    cat = Carnivore("Paddy", 3, "Lion")
    print(cat)

def test_create_enclosure():
    reptile1 = Enclosure("Reptile House", "Terrarium", 20)
    print(reptile1)

def test_create_staff():
    vet = Veterinarian("Joe Boggs", 2025)
    zookeeper = Zookeeper("Sally Fubbs", 2025)
    print(vet)
    print(zookeeper)

def test_create_zoo():
    """
    Direct tests for the Zoo class for zoo creation, setting attributes and string display.

    Tests:
        - Creation of a zoo instance.
        - Changing **attributes** manually.
        - Displaying string representations.

     Expected behaviour:
        - Zoo should be created successfully.
        - Valid changes should be applied and displayed in string representation.
        - Invalid changes should not be applied and string representation should be displayed unchanged.
    """
    print("\n=== TEST: Creation of Zoo ===\n")

    # --- Create and display zoo ---
    zoo = Zoo("Halls Gap Zoo")
    print(zoo)

def test_add_enclosure():
    zoo = Zoo("Halls Gap Zoo")
    zoo.add_enclosure("Reptile House", "Terrarium", 20)
    print(zoo)

def main():
    """Calls all the test functions"""

    # --- Testing animal class ---
    test_create_animal()

    # --- Testing enclosure class ---
    test_create_enclosure()

    # --- Testing staff class ---
    test_create_staff()

    # --- Testing zoo class ---
    test_create_zoo()
    test_add_enclosure()

# Call main function to run tests
if __name__ == "__main__":
    main()
