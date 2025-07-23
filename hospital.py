from doctor import Doctor
from patient import Patient
import csv
from colorama import Fore, init

init(autoreset=True)


class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []

        self.load_doctors()
        self.load_patients()

    def load_doctors(self):
        try:
            with open("doctors.csv", newline="") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    id, name, age, gender, specialization, availability = row
                    doctor = Doctor(
                        id, name, int(age), gender, specialization, availability
                    )
                    self.doctors.append(doctor)
        except Exception as e:
            print(f"\n{Fore.RED}❌ Error loading doctors: {e}")

    def load_patients(self):
        try:
            with open("patients.csv", newline="") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    id, name, age, gender, illness, assigned_doctor, bill_amount = row
                    patient = Patient(
                        id,
                        name,
                        int(age),
                        gender,
                        illness,
                        assigned_doctor,
                        float(bill_amount),
                    )
                    self.patients.append(patient)
        except Exception as e:
            print(f"\n{Fore.RED}❌ Error loading patients: {e}")

    def display_doctors(self):
        for d in self.doctors:
            print(d)

    def display_patients(self):
        for p in self.patients:
            print(p)

    def sort_doctors(self):
        try:
            self.doctors.sort(key=lambda doctor: doctor.name)
            with open("doctors.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        "ID",
                        "Name",
                        "Age",
                        "Gender",
                        "Specialization",
                        "Availability",
                    ]
                )
                for d in self.doctors:
                    writer.writerow(
                        [
                            d.id,
                            d.name,
                            d.age,
                            d.gender,
                            d.specialization,
                            d.availability,
                        ]
                    )

            print(f"\n{Fore.CYAN}✅ Doctors sorted successfully! 🧑‍⚕️")
        except Exception as e:
            print(f"\n{Fore.RED}❌ Failed to sort doctors: {e}")

    def sort_patients(self):
        try:
            self.patients.sort(key=lambda patient: patient.name)
            with open("patients.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        "ID",
                        "Name",
                        "Age",
                        "Gender",
                        "Illness",
                        "AssignedDoctor",
                        "BillAmount",
                    ]
                )
                for p in self.patients:
                    writer.writerow(
                        [
                            p.id,
                            p.name,
                            p.age,
                            p.gender,
                            p.illness,
                            p.assigned_doctor,
                            p.bill_amount,
                        ]
                    )

            print(f"\n{Fore.RED}✅ Patients sorted successfully! 🩺")
        except Exception as e:
            print(f"\n{Fore.RED}❌ Failed to sort patients: {e}")

    def generate_new_doctor_id(self):
        if not self.doctors:
            return "D001"
        last_num = max(int(doc.id[1:]) for doc in self.doctors)
        return f"D{last_num + 1:03d}"

    def generate_new_patient_id(self):
        existing_ids = sorted(int(p.id[1:]) for p in self.patients)
        new_id = 1
        for eid in existing_ids:
            if eid == new_id:
                new_id += 1
            else:
                break
        return f"P{new_id:03d}"

    def add_doctor(self):
        new_id = self.generate_new_doctor_id()
        try:
            name = input(f"{Fore.CYAN}Enter Doctor Name: ")
            age = int(input(f"{Fore.CYAN}Enter Age: "))
            gender = input(f"{Fore.CYAN}Enter Gender: ")
            specialization = input(f"{Fore.CYAN}Enter Specialization: ")
            availability = input(f"{Fore.CYAN}Is the doctor available? (Yes/No): ")
        except ValueError:
            print(f"\n{Fore.RED}❌ Invalid input. Doctor not added.")
            return

        doctor = Doctor(new_id, name, age, gender, specialization, availability)

        self.doctors.append(doctor)

        try:
            with open("doctors.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        doctor.id,
                        doctor.name,
                        doctor.age,
                        doctor.gender,
                        doctor.specialization,
                        doctor.availability,
                    ]
                )
            print(f"\n{Fore.GREEN}✅ Doctor added successfully! 🧑‍⚕️")
        except Exception as e:
            print(f"\n{Fore.RED}❌ Failed to save doctor: {e}")

    def add_patient(self):
        print(f"\n{Fore.YELLOW}👤 Adding New Patient...\n")

        name = input(f"{Fore.RED}Enter Name: ")
        age = input(f"{Fore.RED}Enter Age: ")
        gender = input(f"{Fore.RED}Enter Gender: ")
        illness = input(f"{Fore.RED}Enter Illness: ")
        assigned_doctor = input(
            f"{Fore.RED}Enter which Doctor to assign (ID or leave empty): "
        ).strip()

        # Handle None or blank assignment
        if not assigned_doctor or assigned_doctor.lower() == "none":
            assigned_doctor = "None"
        else:
            doctor_found = False
            for doctor in self.doctors:
                if doctor.id == assigned_doctor:
                    doctor_found = True
                    if doctor.availability.lower() == "yes":
                        doctor.availability = "No"
                        break
                    else:
                        print(
                            f"\n{Fore.RED}❌ Doctor is not available. Please choose another one."
                        )
                        return
            if not doctor_found:
                print(f"\n{Fore.RED}❌ Doctor with ID {assigned_doctor} not found!")
                return

        # Generate reusable patient ID
        used_ids = {int(p.id[1:]) for p in self.patients}
        new_id_num = 1
        while new_id_num in used_ids:
            new_id_num += 1
        new_id = f"P{new_id_num:03d}"

        try:
            bill_amount = float(input(f"{Fore.RED}Enter Bill Amount: "))
        except ValueError:
            print(f"\n{Fore.RED}❌ Invalid bill amount! Please enter a number.")
            return

        new_patient = Patient(
            new_id, name, age, gender, illness, assigned_doctor, bill_amount
        )
        self.patients.append(new_patient)

        try:
            with open("patients.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        "ID",
                        "Name",
                        "Age",
                        "Gender",
                        "Illness",
                        "AssignedDoctor",
                        "BillAmount",
                    ]
                )
                for p in self.patients:
                    writer.writerow(
                        [
                            p.id,
                            p.name,
                            p.age,
                            p.gender,
                            p.illness,
                            p.assigned_doctor,
                            p.bill_amount,
                        ]
                    )

            with open("doctors.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["ID", "Name", "Age", "Gender", "Specialization", "Availability"]
                )
                for d in self.doctors:
                    writer.writerow(
                        [
                            d.id,
                            d.name,
                            d.age,
                            d.gender,
                            d.specialization,
                            d.availability,
                        ]
                    )

            print(f"\n{Fore.GREEN}✅ Patient {new_id} added successfully!\n")
        except Exception as e:
            print(f"\n{Fore.RED}❌ Error while saving patient: {e}")

    def edit_doctor(self):
        id = input(f"{Fore.CYAN}Enter the ID of the Doctor: ")

        found = False
        for doctor in self.doctors:
            if doctor.id == id:
                print(f"\n{Fore.GREEN}Doctor found: {doctor} 🧑‍⚕️\n")
                availability = input(f"{Fore.CYAN}Enter new Availability (Yes/No): ")
                doctor.availability = availability

                try:
                    with open("doctors.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            [
                                "ID",
                                "Name",
                                "Age",
                                "Gender",
                                "Specialization",
                                "Availability",
                            ]
                        )
                        for d in self.doctors:
                            writer.writerow(
                                [
                                    d.id,
                                    d.name,
                                    d.age,
                                    d.gender,
                                    d.specialization,
                                    d.availability,
                                ]
                            )

                    print(
                        f"\n{Fore.GREEN}✅ Doctor availability updated successfully! 🔄"
                    )
                except Exception as e:
                    print(f"\n{Fore.RED}❌ Failed to update doctor: {e}")
                found = True
                break

        if not found:
            print(f"\n{Fore.RED}❌ Doctor with ID: {id} not found! ⚠️")

    def edit_patient(self):
        id = input(f"{Fore.CYAN}Enter the ID of the Patient: ")

        found = False
        for patient in self.patients:
            if patient.id == id:
                print(f"\n{Fore.GREEN}Patient found: {patient} 🧑‍💻")

                print(
                    f"""\n{Fore.YELLOW}
                        1.Update Bill Amount
                        2.Change Assigned Doctor (with availability check)
                        3.Update Illness\n"""
                )

                try:
                    choice = int(input(f"{Fore.RED}Enter your choice: "))
                except ValueError:
                    print(f"{Fore.RED}❌ Please choose option as integer (1, 2, 3)!\n")
                    return

                if choice == 1:
                    try:
                        new_bill_amount = float(
                            input(f"{Fore.RED}Enter the new Bill Amount: ")
                        )
                        patient.bill_amount = new_bill_amount
                    except ValueError:
                        print(f"\n{Fore.RED}❌ Invalid amount!")
                        return

                elif choice == 2:
                    new_doctor_id = input(
                        f"{Fore.RED}Enter the new Doctor ID to assign (or type None to unassign): "
                    ).strip()

                    # Handle unassignment (None, none, blank)
                    if new_doctor_id.lower() == "none" or new_doctor_id == "":
                        # Reset current doctor's availability
                        for doc in self.doctors:
                            if doc.id == patient.assigned_doctor:
                                doc.availability = "Yes"
                                break
                        patient.assigned_doctor = "None"
                        print(f"\n{Fore.YELLOW}👤 Doctor unassigned from patient.")
                    else:
                        doctor_found = False
                        for doctor in self.doctors:
                            if doctor.id == new_doctor_id:
                                doctor_found = True
                                if doctor.availability.lower() == "yes":
                                    # Reset previous doctor's availability
                                    for doc in self.doctors:
                                        if doc.id == patient.assigned_doctor:
                                            doc.availability = "Yes"
                                            break

                                    # Assign new doctor and mark unavailable
                                    patient.assigned_doctor = new_doctor_id
                                    doctor.availability = "No"
                                    print(
                                        f"\n{Fore.GREEN}✅ Doctor assigned successfully!"
                                    )
                                else:
                                    print(f"\n{Fore.RED}❌ Doctor not available! ⚠️")
                                break

                        if not doctor_found:
                            print(
                                f"\n{Fore.RED}❌ Doctor with ID {new_doctor_id} not found! ⚠️"
                            )

                elif choice == 3:
                    new_illness = input(f"{Fore.RED}Enter the new illness: ")
                    patient.illness = new_illness

                else:
                    print(f"{Fore.RED}❌ Invalid choice!\n")
                    return

                try:
                    with open("patients.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            [
                                "ID",
                                "Name",
                                "Age",
                                "Gender",
                                "Illness",
                                "AssignedDoctor",
                                "BillAmount",
                            ]
                        )
                        for p in self.patients:
                            writer.writerow(
                                [
                                    p.id,
                                    p.name,
                                    p.age,
                                    p.gender,
                                    p.illness,
                                    p.assigned_doctor,
                                    p.bill_amount,
                                ]
                            )

                    with open("doctors.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            [
                                "ID",
                                "Name",
                                "Age",
                                "Gender",
                                "Specialization",
                                "Availability",
                            ]
                        )
                        for d in self.doctors:
                            writer.writerow(
                                [
                                    d.id,
                                    d.name,
                                    d.age,
                                    d.gender,
                                    d.specialization,
                                    d.availability,
                                ]
                            )

                    print(f"\n{Fore.GREEN}✅ Patient details updated successfully! 🔁")
                except Exception as e:
                    print(f"\n{Fore.RED}❌ Error while saving updates: {e}")
                found = True
                break

        if not found:
            print(f"\n{Fore.RED}❌ Patient with ID: {id} not found! ⚠️")

    def delete_doctor(self):
        doctor_id = input(f"{Fore.RED}\nEnter the Doctor ID to delete: ")
        found = False

        for doctor in self.doctors:
            if doctor.id == doctor_id:
                found = True

                # Check if any patient is assigned to this doctor
                assigned_patients = [
                    patient
                    for patient in self.patients
                    if patient.assigned_doctor == doctor_id
                ]
                if assigned_patients:
                    print(
                        f"{Fore.YELLOW}\n❌ Doctor cannot be deleted as they are currently assigned to a patient.\n"
                    )
                    return

                # If not assigned, delete doctor
                self.doctors.remove(doctor)

                # Save updated doctor list to CSV
                with open("doctors.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        [
                            "ID",
                            "Name",
                            "Age",
                            "Gender",
                            "Specialization",
                            "Availability",
                        ]
                    )
                    for d in self.doctors:
                        writer.writerow(
                            [
                                d.id,
                                d.name,
                                d.age,
                                d.gender,
                                d.specialization,
                                d.availability,
                            ]
                        )

                print(f"{Fore.GREEN}\n✅ Doctor deleted successfully.\n")
                return

        if not found:
            print(f"{Fore.RED}\n❌ Doctor with ID {doctor_id} not found.\n")

    def delete_patient(self):
        patient_id = input(f"{Fore.RED}\nEnter the Patient ID to delete: ")
        found = False

        for i, patient in enumerate(self.patients):
            if patient.id == patient_id:
                found = True
                assigned_doctor_id = patient.assigned_doctor

                # Mark assigned doctor as available again in list
                for doctor in self.doctors:
                    if doctor.id == assigned_doctor_id:
                        doctor.availability = "Yes"
                        break

                # Remove patient from list
                del self.patients[i]

                # Save updated patient list to CSV
                with open("patients.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        [
                            "ID",
                            "Name",
                            "Age",
                            "Gender",
                            "Illness",
                            "AssignedDoctor",
                            "BillAmount",
                        ]
                    )
                    for p in self.patients:
                        writer.writerow(
                            [
                                p.id,
                                p.name,
                                p.age,
                                p.gender,
                                p.illness,
                                p.assigned_doctor,
                                p.bill_amount,
                            ]
                        )

                # Save updated doctor list to CSV
                with open("doctors.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        [
                            "ID",
                            "Name",
                            "Age",
                            "Gender",
                            "Specialization",
                            "Availability",
                        ]
                    )
                    for d in self.doctors:
                        writer.writerow(
                            [
                                d.id,
                                d.name,
                                d.age,
                                d.gender,
                                d.specialization,
                                d.availability,
                            ]
                        )

                print(
                    f"{Fore.GREEN}\n✅ Patient deleted and assigned doctor is now available.\n"
                )
                break

        if not found:
            print(f"{Fore.RED}\n❌ Patient with ID {patient_id} not found.\n")
