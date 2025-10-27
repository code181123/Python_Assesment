from app.models.ticket import Ticket
# import time
def create_ticket(id, patient_id ):
    if patient_id is None:
        raise ValueError("Failed")
    return Ticket(id, patient_id)

# def process_ticket(ticket, doctor):
#     if doctor.available:
#         doctor.assign_ticket(ticket)
#         ticket.doctor_id = doctor.id
#         time.sleep(10)
#         ticket.close_ticket()
#         return success_msg
#     else:
#         raise Exception("Doctor not available to process the ticket")

# def write_ticket_to_file(ticket, filepath):
#     with open(filepath, 'w') as f:
#         f.write(f"Ticket ID: {ticket.id}, Patient ID: {ticket.patient_id}, Doctor ID: {ticket.doctor_id}, Status: {ticket.status}\n")

