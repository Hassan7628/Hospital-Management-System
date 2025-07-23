class Doctor:
    def __init__(self, id, name, age, gender, specialization, availability):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.specialization = specialization
        self.availability = availability

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Gender {self.gender}, Specialization: {self.specialization}, Availability {self.availability}"
