from pyfiglet import Figlet
from colorama import Fore, init
from hospital import Hospital
from time import sleep

init(autoreset=True)


def menu():
    hospital = Hospital()
    while True:
        sleep(1)
        f = Figlet(font="block")
        banner = f.renderText("+ MENU")
        print(Fore.RED + banner)

        print(
            f"""\n{Fore.YELLOW}
              1.Display Patients
              2.Display Doctors
              3.Add a Patient
              4.Add a Doctor
              5.Sort Patients
              6.Sort Doctors
              7.Remove a Patient
              8.Remove a Doctor
              9.Edit a Patient
              10.Edit a Doctor
              11.Quit Program
              
              \n"""
        )

        try:
            choice = int(input(f"{Fore.MAGENTA}Enter your choice: "))
        except ValueError:
            print(f"{Fore.RED}❌ Please choose option as integer (1 to 11)!\n")
            continue

        if choice == 1:
            print(f"\n{Fore.CYAN}🩺 Displaying all patients:\n")
            hospital.display_patients()

        elif choice == 2:
            print(f"\n{Fore.CYAN}🧑‍⚕️ Displaying all doctors:\n")
            hospital.display_doctors()

        elif choice == 3:
            print(f"\n{Fore.CYAN}🧑‍💻 Adding a new patient...\n")
            hospital.add_patient()

        elif choice == 4:
            print(f"\n{Fore.CYAN}🧑‍⚕️ Adding a new doctor...\n")
            hospital.add_doctor()

        elif choice == 5:
            print(f"\n{Fore.CYAN}🔃 Sorting patients by name...\n")
            hospital.sort_patients()

        elif choice == 6:
            print(f"\n{Fore.CYAN}🔃 Sorting doctors by name...\n")
            hospital.sort_doctors()

        elif choice == 7:
            print(f"\n{Fore.CYAN}🗑️ Removing a patient...\n")
            hospital.delete_patient()

        elif choice == 8:
            print(f"\n{Fore.CYAN}🗑️ Removing a doctor...\n")
            hospital.delete_doctor()

        elif choice == 9:
            print(f"\n{Fore.CYAN}📝 Editing patient details...\n")
            hospital.edit_patient()

        elif choice == 10:
            print(f"\n{Fore.CYAN}📝 Editing doctor details...\n")
            hospital.edit_doctor()

        elif choice == 11:
            print(f"\n{Fore.GREEN}✅ You are exiting the program! Goodbye 👋")
            break

        else:
            print(f"\n{Fore.RED}❌ Invalid Choice! Please choose between 1 to 11.\n")


if __name__ == "__main__":
    menu()
