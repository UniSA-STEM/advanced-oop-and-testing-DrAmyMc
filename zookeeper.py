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
    # Behavioural methods
    # -------------------

    def clean_enclosure(self, enclosure_name):
        pass

    def feed_animals(self, species):
        pass