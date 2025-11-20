"""
File: zookeeper.py
Description: Zookeeper child class from Staff parent class, for use in a Zoo.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Staff


class Zookeeper(Staff):
    """A zookeeper with responsibilities and behaviours unique to the zookeeper role, extending Staff."""

    def __init__(self, staff_id, first_name, last_name, date_hired):
        """
        Initialises a new Zookeeper instance of the Zookeeper subclass.

        Notes:
            Attributes such as staff_id, first_name, last_name, and date_hired are initialised by the parent class.
        """
        super().__init__(staff_id, first_name, last_name, date_hired)
        self._responsibilities = ['Feed animals', 'Clean enclosures', 'Exhibit planning']

    # -------------------
    # Helper methods
    # -------------------

    def search_assigned_enclosures(self, enclosure_name)-> object | None:
        """Returns the assigned enclosure if found in the assigned enclosure list, otherwise None."""
        for enclosure in self.assigned_enclosures:
            if enclosure.name == enclosure_name:
                return enclosure

    # -------------------
    # Behavioural methods
    # -------------------

    def clean_enclosure(self, enclosure_name):
        """Cleans the enclosure if assigned and it needs cleaning."""
        enclosure = self.search_assigned_enclosures(enclosure_name)
        # Will not clean enclosure if not assigned
        if enclosure is None:
            return f"Cannot clean {enclosure_name}. Not assigned to this enclosure."
        # Will not clean enclosure if pristine
        elif enclosure.cleanliness_level == 5:
            return f"Cannot clean {enclosure_name}. This enclosure is already pristine."
        # Clean enclosure if assigned and not pristine
        else:
            enclosure.clean_enclosure()
            return f"{self.first_name} {self.last_name} cleaned the {enclosure.name} enclosure."

    def feed_animals(self, enclosure_name):
        """Feeds the animals in an enclosure if assigned and it contains animals."""
        enclosure = self.search_assigned_enclosures(enclosure_name)
        # Will not feed animals if not assigned
        if enclosure is None:
            return f"Cannot feed animals in {enclosure_name}. Not assigned to this enclosure."
        # Will not feed animals if enclosure is empty
        elif enclosure.animal_type is None:
            return f"Cannot feed animals in {enclosure_name}. This enclosure is empty."
        # Feeds animals if assigned to enclosure and animals present
        else:
            feed = enclosure.lookup_feed()
            return f"{self.first_name} {self.last_name} fed {feed} to the {enclosure.animal_type}s in {enclosure.name}."