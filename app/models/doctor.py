class Doctor:
    def __init__(self, id: int, name: str, specialization: str, available: bool = True):
        self.id: int = id
        self.name: str = name
        self.specialization: str = specialization
        self.available:bool= available

    def assign_ticket(self, ticket):
        if not self.available:
            raise Exception("Doctor not available")
    def __repr__(self) -> str:
        return (
            f"Doctor(id={self.id!r}, name={self.name!r}, "
            f"specialization={self.specialization!r}, available={self.available})"
        )
        
        
        return f"Assigned ticket {ticket.id} to doctor {self.name}"
