from app.models.ticket import Ticket

def create_ticket(id, patient_id, doctor_id):
    # BUG: doctor_id is sometimes None due to matching logic error
    if doctor_id is None:
        raise ValueError("Doctor assignment failed")
    return Ticket(id, patient_id, doctor_id)
