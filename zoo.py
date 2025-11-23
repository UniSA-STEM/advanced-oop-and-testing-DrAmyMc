"""
File: zoo.py
Description: Zoo class, representing a zoo and its operations with enclosures, animals, and staff.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""
from ftplib import all_errors

from animal import Animal
from enclosure import Enclosure
from staff import Staff


class Zoo:
    """
    Represents a zoo, with enclosures, animals and staff.
    """

    def __init__(self, name):
        """
        Initialises a new Zoo instance.
        Args: name (str): The name of the zoo.
        """
        self.name = name
        self.__animals = set()
        self.__enclosures = set()
        self.__staff = set()

    # --------------
    # Getter methods
    # --------------

    def get_name(self) -> str:
        """Returns the zoo's name."""
        return self.__name

    def get_animals(self) -> set:
        """Returns the set of animal objects at the zoo."""
        return self.__animals

    def get_enclosures(self) -> set:
        """Returns the set of enclosure objects at the zoo."""
        return self.__enclosures

    def get_staff(self) -> set:
        """Returns the set of staff objects at the zoo."""
        return self.__staff

    # --------------
    # Setter methods
    # --------------

    def set_name(self, name):
        """
        Sets the zoo's name.
        Args: name (str): The zoo name, ensuring only a string of a minimum length may be passed.
        """
        MIN_LENGTH = 3
        if type(name) is str and len(name) >= MIN_LENGTH:
            self.__name = name
        else:
            raise ValueError(f"Invalid zoo name. Please enter text of at least {MIN_LENGTH} characters.")

    # --------------------
    # Property definitions
    # --------------------

    name = property(get_name, set_name)
    animals = property(get_animals)
    enclosures = property(get_enclosures)
    staff = property(get_staff)

    # -------------------
    # Helper methods
    # -------------------

    def lookup_animal(self, animal_name, species) -> Animal | None:
        """Looks up animal by name and species from animals set, returns animal object if found."""
        target = None
        for animal in self.animals:
            if animal.name == animal_name and animal.species == species:
                target = animal
        return target

    def lookup_enclosure(self, enclosure_name) -> Enclosure | None:
        """Looks up enclosure by name from enclosures set, returns enclosure object if found."""
        target = None
        for enclosure in self.enclosures:
            if enclosure.name == enclosure_name:
                target = enclosure
        return target

    def lookup_staff(self, staff_id) -> Staff | None:
        """Looks up staff by staff_id from staff set, returns staff object if found."""
        target = None
        for staff in self.staff:
            if staff.staff_id == staff_id:
                target = staff
        return target

    # -------------------
    # Behavioural methods
    # -------------------

    def add_animal(self, animal) -> str:
        """Adds an animal object to the set of animals at the zoo."""
        if isinstance(animal, Animal):
            self.__animals.add(animal)
            return f"{animal.name} the {animal.species} added to the zoo."
        else:
            raise TypeError(f"Invalid object - must be an Animal object to add to animals.")

    def add_enclosure(self, enclosure) -> str:
        """Adds an enclosure object to the set of enclosures at the zoo."""
        if isinstance(enclosure, Enclosure):
            self.__enclosures.add(enclosure)
            return f"{enclosure.name} enclosure added to the zoo."
        else:
            raise TypeError(f"Invalid object - must be an Enclosure object to add to enclosures.")

    def add_staff(self, staff) -> str:
        """Adds a staff object to the set of staff at the zoo."""
        if isinstance(staff, Staff):
            self.__staff.add(staff)
            return f"{staff.role} {staff.first_name} {staff.last_name} added to the zoo."
        else:
            raise TypeError(f"Invalid object - must be a Staff object to add to staff.")

    def remove_animal(self, animal_name, species) -> str:
        """Removes animal from the set of animals at the zoo if found. Also removes animal from assigned enclosure."""
        target = self.lookup_animal(animal_name, species)
        if target:
            self.animals.remove(target)
            # Also remove animal from any enclosure where animal is housed
            for enclosure in self.enclosures:
                if target in enclosure.animals_housed:
                    enclosure.animals_housed.remove(target)
            return f"{target.name} the {target.species} removed from the zoo."
        else:
            raise ValueError(f"{animal_name} the {species} does not exist.")

    def remove_enclosure(self, enclosure_name) -> str:
        """Removes enclosure from the set of enclosures at the zoo if found. Also removes from staff assignments."""
        target = self.lookup_enclosure(enclosure_name)
        if target:
            self.enclosures.remove(target)
            # Also remove enclosure from any staff assigned enclosure list
            for staff in self.staff:
                if target in staff.assigned_enclosures:
                    staff.assigned_enclosures.remove(target)
            return f"{target.name} enclosure removed from the zoo."
        else:
            raise ValueError(f"Enclosure with name {enclosure_name} does not exist.")

    def remove_staff(self, staff_id) -> str:
        """Removes staff from the set of staff at the zoo if found. Also updates any enclosure assignments."""
        target = self.lookup_staff(staff_id)
        if target:
            self.staff.remove(target)
            # Also remove from any enclosure assignments
            for enclosure in self.enclosures:
                if target == enclosure.assigned_vet:
                    enclosure.assigned_vet = None
                if target == enclosure.assigned_keeper:
                    enclosure.assigned_keeper = None
            return f"{target.role} {target.first_name} {target.last_name} removed from the zoo."
        else:
            raise ValueError(f"Staff with staff id {staff_id} does not exist.")

    def assign_animal_to_enclosure(self, animal_name, species, enclosure_name):
        animal = self.lookup_animal(animal_name, species)
        enclosure = self.lookup_enclosure(enclosure_name)
        if animal is None:
            raise ValueError(f"{animal_name} the {species} does not exist.")
        elif enclosure is None:
            raise ValueError(f"Enclosure with name {enclosure_name} does not exist.")
        elif not animal.on_display:
            raise ValueError(f"Cannot move this animal while under treatment for a health condition.")
        else:
            enclosure.add_assigned_animal(animal)
            # Removes from any other enclosure currently assigned to
            for other in self.enclosures:
                if other is not enclosure and animal in other.animals_housed:
                    other.animals_housed.remove(animal)
            return f"{animal.name} the {animal.species} is now assigned to the {enclosure.name} enclosure."

    def assign_enclosure_to_staff(self, enclosure_name, staff_id):
        enclosure = self.lookup_enclosure(enclosure_name)
        staff = self.lookup_staff(staff_id)
        if enclosure is None:
            raise ValueError(f"Enclosure with name {enclosure_name} does not exist.")
        elif staff is None:
            raise ValueError(f"Staff with staff id {staff_id} does not exist.")
        else:
            staff.add_assigned_enclosure(enclosure)
            # Removes enclosure from any other staff members it is currently assigned to
            for other_staff in self.staff:
                if other_staff is not staff and staff.role == other_staff.role:
                    if enclosure in other_staff.assigned_enclosures:
                        other_staff.assigned_enclosures.remove(enclosure)
            # Updates assignment in enclosure
            if staff.role == 'Zookeeper':
                enclosure.assigned_keeper = staff
            if staff.role == 'Veterinarian':
                enclosure.assigned_vet = staff
            return (f"{staff.first_name} {staff.last_name} is now the assigned {staff.role} for "
                    f"the {enclosure.name} enclosure.")

    def schedule_feeding(self):
        """
        Schedules feeding of all enclosures in the zoo by their assigned zookeepers.
        Calls each Zookeeper's feed_animals method for each assigned enclosure.
        Returns: a summary of feeding actions.
        """
        details = [f'---FEEDING TIME AT {self.name.upper()}---']
        for staff in self.staff:
            if staff.role == 'Zookeeper':
                for enclosure in staff.assigned_enclosures:
                    str = staff.feed_animals(enclosure.name)
                    details.append(str)
        details.append('')
        return '\n'.join(details)

    def schedule_cleaning(self):
        """
        Schedules cleaning of all enclosures in the zoo by their assigned zookeepers.
        Calls each Zookeeper's clean_enclosure method for each assigned enclosure.
        Returns: a summary of cleaning actions.
        """
        details = [f'---CLEANING TIME AT {self.name.upper()}---']
        for staff in self.staff:
            if staff.role == 'Zookeeper':
                for enclosure in staff.assigned_enclosures:
                    str = staff.clean_enclosure(enclosure.name)
                    details.append(str)
        details.append('')
        return '\n'.join(details)

    def schedule_health_checks(self):
        """
        Schedules health checks of all enclosures in the zoo by their assigned veterinarians.
        Calls each Veterinarian's conduct_health_checks method for each assigned enclosure.
        Returns: a summary of health check actions.
        """
        details = [f'---HEALTH CHECK TIME AT {self.name.upper()}---']
        for staff in self.staff:
            if staff.role == 'Veterinarian':
                for enclosure in staff.assigned_enclosures:
                    str = staff.conduct_health_checks(enclosure.name)
                    details.append(str)
        details.append('')
        return '\n'.join(details)

    def list_animal_health_history(self, animal_name, species):
        """Lists health history for a particular animal."""
        target = self.lookup_animal(animal_name, species)
        if target:
            details = [f'---HEALTH HISTORY FOR {target.name.upper()} THE {target.species.upper()}---\n']
            if target.health_record == []:
                details.append('No health records found.')
            else:
                for record in target.health_record:
                    details.append(str(record))
            return '\n'.join(details)
        else:
            raise ValueError(f"{animal_name} the {species} does not exist.")

    def list_animals_under_treatment(self):
        details = [f'---ANIMALS CURRENTLY UNDER TREATMENT---']
        under_treatment = []
        for animal in self.animals:
            for record in animal.health_record:
                if record.is_current:
                    under_treatment.append((animal, record))
        if not under_treatment:
            details.append('No current health records found.')
        else:
            for animal, record in under_treatment:
                sex = 'Female' if animal.is_female else 'Male'
                severity = ['Negligible', 'Minor', 'Moderate', 'Severe'][record.severity_level]
                issue = record.issue_type
                details.append(f"{animal.name}, {animal.species}, {sex}, aged {animal.age} years, {severity} {issue}")
        details.append('')
        return '\n'.join(details)

    def list_animals_by_species(self):
        details = [f'---ANIMALS IN ZOO LISTED BY SPECIES---']
        if not self.animals:
            details.append('No animals found.')
        else:
            zoo_species = set()
            for animal in self.animals:
                zoo_species.add(animal.species)
            sorted_species = sorted(zoo_species)
            for species in sorted_species:
                details.append(f'{species}:')
                for animal in self.animals:
                    if animal.species == species:
                        sex = 'Female' if animal.is_female else 'Male'
                        details.append(f"   {animal.name}, {sex}, age {animal.age}")
        details.append('')
        return '\n'.join(details)

    def list_enclosures_by_status(self):
        details = [f'---ENCLOSURES IN ZOO LISTED BY CLEANLINESS---']
        if not self.enclosures:
            details.append('No enclosures found.')
        else:
            clean_levels = set()
            for enclosure in self.enclosures:
                clean_levels.add(enclosure.cleanliness_level)
            sorted_levels = sorted(clean_levels)
            desc = ['Filthy (Level 0):', 'Very Dirty (Level 1):', 'Dirty (Level 2):', 'Becoming Dirty (Level 3):',
                    'Quite Clean (Level 4):', 'Pristine (Level 5):']
            for level in sorted_levels:
                details.append(desc[level])
                for enclosure in self.enclosures:
                    if enclosure.cleanliness_level == level:
                        details.append(f"   {enclosure.name}, {enclosure.type}")
            details.append('')
            return '\n'.join(details)

    # def list_enclosures_by_status(self):
    #     details = [f'---ENCLOSURES IN ZOO LISTED BY CLEANLINESS---']
    #     if not self.enclosures:
    #         details.append('No enclosures found.')
    #     else:
    #         level5 = []
    #         level4 = []
    #         level3 = []
    #         level2 = []
    #         level1 = []
    #         level0 = []
    #         for enclosure in self.enclosures:
    #             if enclosure.cleanliness_level == 5:
    #                 level5.append(enclosure)
    #             elif enclosure.cleanliness_level == 4:
    #                 level4.append(enclosure)
    #             elif enclosure.cleanliness_level == 3:
    #                 level3.append(enclosure)
    #             elif enclosure.cleanliness_level == 2:
    #                 level2.append(enclosure)
    #             elif enclosure.cleanliness_level == 1:
    #                 level1.append(enclosure)
    #             else:
    #                 level0.append(enclosure)
    #         if level5:
    #             details.append('Pristine Enclosures (Level 5):')
    #             for enc in level5:
    #                 details.append(f'   {enc.name}')
    #         if level4:
    #             details.append('Quite Clean Enclosures (Level 4):')
    #             for enc in level4:
    #                 details.append(f'   {enc.name}')
    #         if level3:
    #             details.append('Becoming Dirty Enclosures (Level 3):')
    #             for enc in level3:
    #                 details.append(f'   {enc.name}')
    #         if level2:
    #             details.append('Dirty Enclosures (Level 2):')
    #             for enc in level2:
    #                 details.append(f'   {enc.name}')
    #         if level1:
    #             details.append('Very Dirty Enclosures (Level 1):')
    #             for enc in level1:
    #                 details.append(f'   {enc.name}')
    #         if level0:
    #             details.append('Filthy Enclosures (Level 0):')
    #             for enc in level0:
    #                 details.append(f'   {enc.name}')
    #         details.append('')
    #         return '\n'.join(details)

    def __str__(self) -> str:
        """
        Returns a formatted string containing the zoo's details.
        Returns: str: The zoo name and list of animals, enclosures and staff.
        """
        animals = len(self.animals) if self.animals else 'no'
        enclosures = len(self.enclosures) if self.enclosures else 'no'
        staff = len(self.staff) if self.staff else 'no'
        return (f'---{self.name.upper()}---\n'
                f'This zoo has:\n'
                f'   {animals} animals\n'
                f'   {enclosures} enclosures\n'
                f'   {staff} staff\n')
