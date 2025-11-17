'''
File: test_staff.py
Description: A brief description of this Python module.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
'''


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

