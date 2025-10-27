class Doctor:
    def __init__(self, id, name, specialization, available=True):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.available = available

    def assign_ticket(self, ticket):
        if not self.available:
            raise Exception("Doctor not available")
        
        return f"Assigned ticket {ticket.id} to doctor {self.name}"
