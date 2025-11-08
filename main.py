'''
File: main.py
Description: A brief description of this Python module.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
'''

from zoo import Zoo
from enclosure import Enclosure

def test_zoo_creation():
    zoo = Zoo("Halls Gap Zoo")
    print(zoo)

def test_enclosure_creation():
    reptile1 = Enclosure("Reptile House", 20)
    print(reptile1)

def test_add_enclosure():
    zoo = Zoo("Halls Gap Zoo")
    zoo.add_enclosure("Reptile House", 20)
    print(zoo)

def main():
    test_zoo_creation()
    test_enclosure_creation()
    test_add_enclosure()

if __name__ == "__main__":
    main()
