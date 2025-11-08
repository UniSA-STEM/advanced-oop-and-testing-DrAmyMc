'''
File: main.py
Description: A brief description of this Python module.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
'''
from staff import Veterinarian
from staff import Zookeeper
from zoo import Zoo
from enclosure import Enclosure

def test_zoo_creation():
    zoo = Zoo("Halls Gap Zoo")
    print(zoo)

def test_enclosure_creation():
    reptile1 = Enclosure("Reptile House", "Terrarium", 20)
    print(reptile1)

def test_add_enclosure():
    zoo = Zoo("Halls Gap Zoo")
    zoo.add_enclosure("Reptile House", "Terrarium", 20)
    print(zoo)

def test_staff_creation():
    vet = Veterinarian("Joe Boggs", 2025)
    zookeeper = Zookeeper("Sally Fubbs", 2025)
    print(vet)
    print(zookeeper)

def main():
    test_zoo_creation()
    test_enclosure_creation()
    test_add_enclosure()
    test_staff_creation()

if __name__ == "__main__":
    main()
