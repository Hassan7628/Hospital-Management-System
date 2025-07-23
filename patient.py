class Patient:
    def __init__(self, id, name, age, gender, illness, assigned_doctor, bill_amount):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.illness = illness
        self.assigned_doctor = assigned_doctor
        self.bill_amount = float(bill_amount)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Gender {self.gender}, Illness: {self.illness}, Assigned_doctor: {self.assigned_doctor}, Bill_Amount {self.bill_amount}"
