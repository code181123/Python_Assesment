class Ticket:
    def __init__(self, id, patient_id, doctor_id, status="open"):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.status = status

    def close_ticket(self):
        if self.status == "closed":
            raise Exception("Ticket already closed")
        self.status = "closed"
