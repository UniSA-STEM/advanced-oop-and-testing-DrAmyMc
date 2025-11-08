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
from animal import Carnivore


def test_create_zoo():
    zoo = Zoo("Halls Gap Zoo")
    print(zoo)

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

def test_add_enclosure():
    zoo = Zoo("Halls Gap Zoo")
    zoo.add_enclosure("Reptile House", "Terrarium", 20)
    print(zoo)

def main():
    test_create_zoo()
    test_create_animal()
    test_create_enclosure()
    test_create_staff()
    test_add_enclosure()

if __name__ == "__main__":
    main()
