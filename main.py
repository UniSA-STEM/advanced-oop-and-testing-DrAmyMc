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


def main():

    # --- Create instances of a zoo, staff, enclosures, and animals, display empty zoo information ---
    zoo = Zoo("Halls Gap Zoo")
    vetA = Veterinarian(123456, 'Mick', 'Rooney', '20/11/2025')
    zookeeperA = Zookeeper(123457, 'Nick', 'Mooney', '18/11/2025')
    encA = Enclosure('Penguin Land', 'Aquatic', 100)
    encB = Enclosure('African Plains', 'Savannah', 1000)
    birdA = Bird('Percy', 3, False, 'Pelican', 1.5, False)
    birdB = Bird('Evil', 1, True, 'Ostrich', 3.2, True)
    reptileA = Reptile("Lizzie", 1, False, "Lace Monitor", 18, False)
    reptileB = Reptile('Hissy', 3, True, 'Brown Snake', 21, True)
    mammalA = Mammal('Paddy', 3, False, 'Lion', 'Shaggy')
    mammalB = Mammal('Blinky', 1, True, 'Koala', 'Short')
    #print(zoo)
    print(mammalA)
    print(mammalB)
    print(birdA)
    print(birdB)
    print(reptileA)
    print(reptileB)

    # --- Add staff, enclosures and animals, display zoo information ---
    # zoo.add_staff(vetA)
    # zoo.add_staff(zookeeperA)
    # zoo.add_enclosure(encA)
    # zoo.add_enclosure(encB)
    # zoo.add_animal(birdA)
    # zoo.add_animal(reptileA)
    # zoo.add_animal(mammalA)
    # zoo.add_animal(birdB)
    # zoo.add_animal(reptileB)
    # zoo.add_animal(mammalB)
    #print(zoo)

    # --- Remove staff, enclosure, and animals, display zoo information ---
    # zoo.remove_staff(123457)
    # zoo.remove_enclosure('Penguin Land')
    # zoo.remove_animal('Hissy', 'Brown Snake')
    # print(zoo)

    # --- Assign animals to enclosures ---
    #zoo.assign_animal_to_enclosure('Paddy', 'Lion', 'African Plains')


# Call main function to run tests
if __name__ == "__main__":
    main()
