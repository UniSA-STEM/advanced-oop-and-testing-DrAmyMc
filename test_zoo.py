'''
File: test_zoo.py
Description: A brief description of this Python module.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
'''

class TestZoo:
    pass

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
