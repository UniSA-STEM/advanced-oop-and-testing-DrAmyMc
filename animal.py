'''
File: animal.py
Description: A brief description of this Python module.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

#Mammal
    #Kangaroo
        #WesternGreyKangaroo
        #KIKangaroo
    #Carnivore
        #SpottedHyena
        #Lion
#Reptile
    #Snake
        #EasternBrownSnake
        #TigerSnake
    #Lizard
        #Gila Monster
        #BlueTongue
#Bird
    #Flight
        #RainbowLorikeet
        #SulphurCrestedCockatoo
    #Flightless
        #Emu
        #Cassowary

class Animal(ABC):
    def __init__(self, name, age, species):
        self.__name = name
        self.__age = age
        self.__species = species
        #abstract?

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_species(self):
        return self.__species

    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 150:
            self.__age = age

    name = property(get_name)
    age = property(get_age, set_age)
    species = property(get_species)

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def __str__(self):
        return "I am an animal."

class Carnivore(Animal):
    def __init__self(self, name, age, species, space=20):
        super().__init__(name, age, species)
        self.__dietary_requirements = ["fresh meat"]
        self.__space = space
    # Space tied to species?s

    def __str__(self):
        return super().__str__() + f" I am a carnivore, of the species {self.species} species with blah blah."


