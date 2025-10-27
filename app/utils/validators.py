def validate_patient_data(patient):
    if not patient.name:
        raise ValueError("Patient name is required")
    if patient.age < 0:
        raise ValueError("Invalid age")
