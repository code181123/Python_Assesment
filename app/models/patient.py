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
