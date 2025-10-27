from app.models.doctor import Doctor
from app.models.ticket import Ticket

def test_doctor_assignment():
    doc = Doctor(1, "Dr. House", "General")
    ticket = Ticket("T002", 1, None)
    doc.assign_ticket(ticket)
    assert ticket.doctor_id == doc.id  # currently fails
