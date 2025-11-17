"""
File: healthrecord.py
Description: Health Record class, to be associated with an animal object.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Integrity Policy.
"""

def test_create_health_record():
    """
    Direct tests for the HealthRecord class for creation of health records.

    Tests:
        - Creation of a Health Record instance (valid and invalid case).
        - Setting attributes manually (valid and invalid cases).
        - Displaying string representations.
    """
    print("\n=== TEST: Creation of Health Record ===\n")

    # --- Create and display valid health record ---
    record = HealthRecord("Injury", 3, "12 Nov 2025",
                          "Laceration on left front leg", "Clean and bandage wound and monitor.")
    print(record)

    # --- Attempt to create health record with invalid type ---
    record2 = HealthRecord("Leg", 3, "12 Nov 2025",
                          "Laceration on left front leg", "Clean and bandage wound and monitor.")
    print(record2)

    # --- Modify health record attributes to valid values ---
    record.issue_type = 'Illness'
    record.severity_level = 0
    record.date_reported = "10 Nov 2025"
    record.description = "Lethargic due to minor fever"
    record.is_current = False
    record.treatment_plan = "Monitor, but no other changes necessary."
    print(record)

    # --- Attempt to modify health record attributes to invalid values ---
    record.issue_type = 'Leg'
    record.severity_level = -1
    record.severity_level = 4
    record.severity_level = "bad"
    record.date_reported = "10th"
    record.description = "Bad"
    record.is_current = "yes"
    record.treatment_plan = "None"
    print(record)

def test_update_health_record():
    """
    Direct tests for the HealthRecord class for updating health records.

    Tests:
        - Updating health record (valid and invalid cases).
        - Displaying string representations.
    """
    print("\n=== TEST: Updating of Health Record ===\n")

    # --- Create and display valid health record ---
    record = HealthRecord("Injury", 3, "12 Nov 2025",
                          "Laceration on left front leg", "Clean and bandage wound and monitor.")
    print(record)

    # --- Add treatment plan notes then resolve issue ---
    record.update_treatment_plan("Change dressing twice daily.")            #Valid
    record.update_treatment_plan("Continue to monitor for two more days.")  #Valid
    record.update_treatment_plan("Ok")                                      #Invalid output, length insufficient
    record.issue_resolved()
    print(record)

def test_add_health_record():
    """
    Tests creation of health records for an animal.

    Tests:
        - Creation of a Health Record instance for a specific animal.
    """
    print("\n=== TEST: Add Health Record to Animal ===\n")

    # --- Create animal ---
    cat = Mammal("Paddy", 3, "Lion", False)
    print(cat)

    # --- Create and display valid health record ---
    cat.add_health_record("Injury", 3, "12 Nov 2025",
                          "Laceration on left front leg", "Clean and bandage wound and monitor.")
