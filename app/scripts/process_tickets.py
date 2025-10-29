import json
import time
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "static_data"
DOCTORS_FILE = DATA_DIR / "doctors.json"
PATIENTS_FILE = DATA_DIR / "patients.json"
TICKETS_FILE = DATA_DIR / "tickets.json"

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def find_available_doctor(doctors):
    for d in doctors:
        if d.get("available", True):
            return d
    return None

def process_all_tickets():
    doctors = load_json(DOCTORS_FILE)
    patients = load_json(PATIENTS_FILE)
    tickets = load_json(TICKETS_FILE)

    print(f"Loaded {len(doctors)} doctors, {len(patients)} patients, {len(tickets)} tickets")

    for ticket in tickets:
        if ticket.get("status") not in ("pending", "open"):
            continue

        print(f"\nTicket {ticket.get('id')} (patient {ticket.get('patient_id')}) - looking for available doctor...")

        
        doctor = find_available_doctor(doctors)
        while doctor is None:
            print("No doctor available right now. Waiting 1s and retrying...")
            time.sleep(1)
            doctor = find_available_doctor(doctors)

        
        doctor["available"] = False
        ticket["doctor_id"] = doctor["id"]
        ticket["status"] = "in_progress"
        print(f"Assigned ticket {ticket.get('id')} to doctor {doctor.get('name')} (id {doctor.get('id')}). Treatment starting...")

        
        time.sleep(10) # Simulate treatment (10 seconds)

        
        ticket["status"] = "completed"
        doctor["available"] = True
        print(f"Completed ticket {ticket.get('id')} by doctor {doctor.get('name')}")

    
    save_json(DOCTORS_FILE, doctors)
    save_json(TICKETS_FILE, tickets)
    print("\nAll tickets processed. Changes saved to doctors.json and tickets.json")

if __name__ == "__main__":
    process_all_tickets()
