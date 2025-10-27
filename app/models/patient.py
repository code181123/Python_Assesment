class Patient:
    def __init__(self, id, name, age, gender, ailment):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.ailment = ailment

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "ailment": self.ailment
        }

#Sample
Patients = [
    Patient(1, "Alice", 29, "F", "Flu"),
    Patient(2, "Bob", 40, "M", "Fracture")
]