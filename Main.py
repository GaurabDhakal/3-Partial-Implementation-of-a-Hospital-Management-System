# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising stored doctors
    doctors = []
    patients = []
    with open("doctors.txt", "r") as file:
        for line in file:
            strippedLine = line.strip().split(",")
            doctors.append(Doctor(strippedLine[0], strippedLine[1], strippedLine[2], strippedLine[3]))

    with open("patients.txt", "r") as file:
        for line in file:
            strippedLine = line.strip().split(",")
            patients.append(Patient(strippedLine[0], strippedLine[1], strippedLine[2], strippedLine[3], strippedLine[4], strippedLine[5], strippedLine[6]))
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'

    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
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

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
           admin.doctor_management(doctors, patients)
        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            admin.view_patient(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3
                    admin.discharge(patients,discharged_patients)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')

        elif op == '3':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            admin.group_patients_by_family(patients)

        elif op == '7':
            admin.appointment(doctors, patients)

        elif op == '8':
            admin.relocate_doctor_to_patient(patients,doctors)

        elif op == '9':
            admin.management_report(doctors,patients)

        elif op == '0':
            # 6 - Quit
            #ToDo5
            print("You have quit the system.")
            running = False

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
