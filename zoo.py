"""
File: zoo.py
Description: Zoo class, representing a zoo and its operations with enclosures, animals, and staff.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal
from enclosure import Enclosure
from staff import Staff
from veterinarian import Veterinarian
from zookeeper import Zookeeper


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

    def get_name(self)->str:
        """Returns the zoo's name."""
        return self.__name

    def get_animals(self)->set:
        """Returns the set of animal objects at the zoo."""
        return self.__animals

    def get_enclosures(self)->set:
        """Returns the set of enclosure objects at the zoo."""
        return self.__enclosures

    def get_staff(self)->set:
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

    def lookup_animal(self, animal_name, species)->Animal | None:
        """Looks up animal by name and species from animals set, returns animal object if found."""
        target = None
        for animal in self.animals:
            if animal.name == animal_name and animal.species == species:
                target = animal
        return target

    def lookup_enclosure(self, enclosure_name)->Enclosure | None:
        """Looks up enclosure by name from enclosures set, returns enclosure object if found."""
        target = None
        for enclosure in self.enclosures:
            if enclosure.name == enclosure_name:
                target = enclosure
        return target

    def lookup_staff(self, staff_id)->Staff | None:
        """Looks up staff by staff_id from staff set, returns staff object if found."""
        target = None
        for staff in self.staff:
            if staff.staff_id == staff_id:
                target = staff
        return target

    # -------------------
    # Behavioural methods
    # -------------------

    def add_animal(self, animal)->str:
        """Adds an animal object to the set of animals at the zoo."""
        if isinstance(animal, Animal):
            self.__animals.add(animal)
            return f"{animal.name} the {animal.species} added to the zoo."
        else:
            raise TypeError(f"Invalid object - must be an Animal object to add to animals.")

    def add_enclosure(self, enclosure)->str:
        """Adds an enclosure object to the set of enclosures at the zoo."""
        if isinstance(enclosure, Enclosure):
            self.__enclosures.add(enclosure)
            return f"{enclosure.name} enclosure added to the zoo."
        else:
            raise TypeError(f"Invalid object - must be an Enclosure object to add to enclosures.")

    def add_staff(self, staff)->str:
        """Adds a staff object to the set of staff at the zoo."""
        if isinstance(staff, Staff):
            self.__staff.add(staff)
            return f"{staff.role} {staff.first_name} {staff.last_name} added to the zoo."
        else:
            raise TypeError(f"Invalid object - must be a Staff object to add to staff.")

    def remove_animal(self, animal_name, species)->str:
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

    def remove_enclosure(self, enclosure_name)->str:
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

    def remove_staff(self, staff_id)->str:
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
        elif any(record.is_current for record in animal.health_record):
            raise ValueError(f"Cannot move this animal while under treatment for a health condition.")
        else:
            enclosure.add_animal(animal)
            # Removes from any other enclosure currently assigned to
            for other in self.enclosures:
                if other is not enclosure and animal in other.animals_housed:
                    other.animals_housed.remove(animal)
            return f"{animal.name} the {animal.species} assigned to {enclosure.name} enclosure."

    def assign_enclosure_to_staff(self, enclosure_name, staff_id):
        enclosure = self.lookup_enclosure(enclosure_name)
        staff = self.lookup_staff(staff_id)
        if enclosure is None:
            raise ValueError(f"Enclosure with name {enclosure_name} does not exist.")
        elif staff is None:
            raise ValueError(f"Staff with staff id {staff_id} does not exist.")
        else:
            staff.add_enclosure(enclosure)
            # Removes enclosure from any other staff members it is currently assigned to
            for other_staff in self.staff:
                if other_staff is not staff and staff.role == other_staff.role:
                    if enclosure in other_staff.assigned_enclosures:
                        other_staff.assigned_enclosures.remove(enclosure)
            # Updates assignment in enclosure
            if staff.role == 'Zookeeper':
                enclosure.assigned_keeper = f"{staff.first_name} {staff.last_name}"
            if staff.role == 'Veterinarian':
                enclosure.assigned_vet = f"{staff.first_name} {staff.last_name}"
            return (f"{staff.first_name} {staff.last_name} is now the assigned {staff.role} for "
                    f"the {enclosure.name} enclosure.")

    def schedule_feeding(self):
        """
        Schedules feeding of all enclosures in the zoo by their assigned zookeepers.
        Calls each Zookeeper's feed_animals method for each assigned enclosure.
        Returns: a summary of feeding actions.
        """
        details = []
        for staff in self.staff:
            if isinstance(staff, Zookeeper):
                for enclosure in staff.assigned_enclosures:
                    str = staff.feed_animals(enclosure.name)
                    details.append(str)
        return '\n'.join(details)

    def schedule_cleaning(self):
        """
        Schedules cleaning of all enclosures in the zoo by their assigned zookeepers.
        Calls each Zookeeper's clean_enclosure method for each assigned enclosure.
        Returns: a summary of cleaning actions.
        """
        details = []
        for staff in self.staff:
            if isinstance(staff, Zookeeper):
                for enclosure in staff.assigned_enclosures:
                    str = staff.clean_enclosure(enclosure.name)
                    details.append(str)
        return '\n'.join(details)

    def schedule_health_check(self):
        """
        Schedules health checks of all enclosures in the zoo by their assigned veterinarians.
        Calls each Veterinarian's conduct_health_checks method for each assigned enclosure.
        Returns: a summary of health check actions.
        """
        details = []
        for staff in self.staff:
            if isinstance(staff, Veterinarian):
                for enclosure in staff.assigned_enclosures:
                    str = staff.conduct_health_checks(enclosure.name)
                    details.append(str)
        return '\n'.join(details)

    def list_animals_by_species(self):
        pass

    def list_enclosure_status(self):
        pass

    def list_animals_under_treatement(self):
        pass

    #TODO: Update with different format to list enclosures and staff properly
    def __str__(self)->str:
        """
        Returns a formatted string containing the zoo's details.
        Returns: str: The name, enclosure list, and staff list.
        """
        return f"{self.name} has {self.enclosures} enclosures and {self.staff} staff.\n"
