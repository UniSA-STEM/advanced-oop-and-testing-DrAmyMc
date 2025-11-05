'''
File: animal.py
Description: A brief description of this Python module.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
from species import species_dict

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
        self.name = name
        self.age = age
        self.species = species
        self.__dietary_requirements = self.lookup_diet()
        self.__space = self.lookup_space()

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_species(self):
        return self.__species

    def get_dietary_requirements(self):
        return self.__dietary_requirements

    def get_space(self):
        return self.__space

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 150:
            self.__age = age

    def set_species(self, species):
        if species in species_dict:
            self.__species = species

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    species = property(get_species, set_species)
    dietary_requirements = property(get_dietary_requirements)
    space = property(get_space)

    def lookup_diet(self):
        return species_dict[self.species][1]

    def lookup_space(self):
        return species_dict[self.species][0]

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
    def __init__self(self, name, age, species):
        super().__init__(name, age, species)

    def make_sound(self):
        return "Roar!"

    def eat(self):
        return f"{self.name} is now eating {self.dietary_requirements}."

    def sleep(self):
        return f"{self.name} is now sleeping."

    def __str__(self):
        return super().__str__() + (f" I am a {self.species.lower()}, a type of carnivore. "
                                    f"My name is {self.name} and I am {self.age} years old.\n"
                                    f"I need to eat {self.dietary_requirements} and I need a space of {self.space} m2.")

cat = Carnivore("Paddy", 100, "Lion")
print(cat)
print(cat.make_sound())
print(cat.eat())
print(cat.sleep())


