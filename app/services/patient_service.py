from app.models.patient import Patient
import json

def load_patients(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return [Patient(**p) for p in data]

def get_patient_by_id(patients, id):
    for p in patients:
        if p.id == id:
            return p
    return None

def save_patients(filepath, patients):
    """
    Save the current list of Patient objects back to the given JSON file.
    """
    data = [p.to_dict() for p in patients]
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def delete_patient(filepath, patient_id):
    """
    Delete a patient by ID from the JSON file.
    Returns True if deleted, False if not found.
    """
    patients = load_patients(filepath)
    updated_patients = [p for p in patients if p.id != patient_id]

    if len(updated_patients) == len(patients):
        return False

    save_patients(filepath, updated_patients)
    return True