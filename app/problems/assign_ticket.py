def assign_ticket(self, ticket):
    doctors = getattr(self, "doctors", None)
    if not doctors:
        raise RuntimeError("No doctors list found on the manager object")
    last_exception = None
    for doctor in doctors:
        if not getattr(doctor, "available", False):
            continue
        try:
            message = doctor.assign_ticket(ticket)
        except Exception as exc:
            last_exception = exc #trying one doctor if other fails
            continue
        try:
            setattr(doctor, "available", False)
        except Exception:
            pass
    return {
            "message": message,
            "doctor_id": getattr(doctor, "id", None),
            "doctor_name": getattr(doctor, "name", None),
        }
    if last_exception:
        raise RuntimeError("Failed to assign ticket: no available doctor ") from last_exception

    raise RuntimeError("No available doctor to assign the ticket")