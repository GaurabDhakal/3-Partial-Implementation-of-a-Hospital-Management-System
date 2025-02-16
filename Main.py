from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def load_doctors():
    """Load doctors from file"""
    doctors = []
    with open("./doctors.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            doctors.append(Doctor(data[0], data[1], data[2], data[3]))
    return doctors

def load_patients():
    """Load patients from file"""
    patients = []
    with open("patients.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            patients.append(Patient(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    return patients

def handle_discharge_option(admin, patients, discharged_patients):
    """Handle the discharge patient option"""
    admin.view_patient(patients)
    while True:
        op = input('Do you want to discharge a patient(Y/N):').lower()
        if op in ['yes', 'y']:
            admin.discharge(patients, discharged_patients)
            break
        elif op in ['no', 'n']:
            break
        print('Please answer by yes or no.')

def process_menu_choice(choice, admin, doctors, patients, discharged_patients):
    """Process the menu choice"""
    if choice == '1':
        admin.doctor_management(doctors, patients)
    elif choice == '2':
        handle_discharge_option(admin, patients, discharged_patients)
    elif choice == '3':
        admin.view_discharge(discharged_patients)
    elif choice == '4':
        admin.assign_doctor_to_patient(patients, doctors)
    elif choice == '5':
        admin.update_details()
    elif choice == '6':
        admin.group_patients_by_family(patients)
    elif choice == '7':
        admin.appointment(doctors, patients)
    elif choice == '8':
        admin.relocate_doctor_to_patient(patients, doctors)
    elif choice == '9':
        admin.management_report(doctors, patients)
    elif choice == '0':
        print("You have quit the system.")
        return False
    else:
        print('Invalid option. Try again')
    return True

def display_menu():
    """Display the main menu"""
    print('Choose the operation:')
    print(' 1- Register/view/update/delete doctor')
    print(' 2- Discharge patients')
    print(' 3- View discharged patient')
    print(' 4- Assign doctor to a patient')
    print(' 5- Update admin detais')
    print(' 6- View patient names grouped by family')
    print(' 7- Appointment')
    print(' 8- Relocate patient to new doctor')
    print(' 9- Management report')
    print(' 0- Quit')

def main():
    """Main function to run the program"""
    doctors = load_doctors()
    patients = load_patients()
    admin = Admin('admin', '123', 'B1 1AB')
    discharged_patients = []

    while not admin.login():
        print('Incorrect username or password.')

    running = True
    while running:
        display_menu()
        choice = input('Option: ')
        running = process_menu_choice(choice, admin, doctors, patients, discharged_patients)

if __name__ == '__main__':
    main()
