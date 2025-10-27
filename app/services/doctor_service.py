from app.models.doctor import Doctor
import json

def load_doctors(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return [Doctor(**d) for d in data]

def find_available_doctor(doctors, specialization):
    for d in doctors:
        if d.specialization == specialization and d.available:
            return d
    return None
