from Doctor import Doctor
from Patient import Patient

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """


    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        print("I am here inside view!")
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')


    def login(self):
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """

        print("-----Login-----")
        #Get the details of the admin
        while True:  # Loop to allow multiple login attempts
            username = input("Enter the username: ").strip()
            password = input("Enter the password: ").strip()

            try:
                with open(R"login.txt", "r") as f:
                    # Read the username and password from the file
                    lines = f.readlines()

                    # Check if the input matches the stored credentials
                    if username == lines[0].strip() and password == lines[1].strip():
                        print("Successfully logged in the system.")
                        return username  # Exit loop on successful login
                    else:
                        print("Invalid username or password. Please try again.")
                        continue

            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break  # Exit loop on unexpected errors

    def find_index(self,index,doctors):

            # check that the doctor id exists
        if index in range(0,len(doctors)):

            return True

        # if the id is not in the list of doctors
        else:
            return False
    def get_random_id(self):
        # id is equivalent to Math.random() in js generates random number
        return id(object())%10000

    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input("Enter the first name of the Doctor: ")
        surname = input("Enter the surname of the Doctor: ")
        speciality = input("Enter the speciality of the Doctor: ")

        return first_name, surname, speciality
    def get_patient_details(self):
        first_name = input("Enter the first name of the patient: ")
        surname = input("Enter the surname of the patient: ")
        age = input("Enter the age of the patient: ")
        ph_number = input("Enter the phone number of the patient: ")
        post_code = input("Enter the post code or address: ")
        patient_id = self.get_random_id()
        symptoms = input("Enter the symptoms of the patient: ")

        return patient_id, first_name, surname, age, ph_number, post_code, symptoms
    def register_doctor(self, doctors):
        # get the doctor details
        print('Enter the doctor\'s details:')
        first_name,surname,speciality = self.get_doctor_details()

        # check if the name is already registered
        name_exists = False
        for doctor in doctors:
            if first_name.strip() == doctor.get_first_name() and surname.strip() == doctor.get_surname():
                print('Name already exists.')
                name_exists = True
                break # save time and end the loop

        if not name_exists:
            doc_id = self.get_random_id()
            new_doctor = Doctor(doc_id,first_name, surname, speciality)
            line_text = f"\n{doc_id},{first_name},{surname},{speciality}" # /n to ensure new line
            with open("doctors.txt", "a") as file:
                file.write(line_text)
            doctors.append(new_doctor)                                       # ... to the list of doctors
            print('Doctor registered.')

    def register_patient(self, patients):
        print('Enter the patient\'s details:')
        patient_id, first_name, surname, age, ph_number, post_code, symptoms = self.get_patient_details()
        new_patient = Patient(patient_id, first_name, surname, age, ph_number, post_code, symptoms)
        line_text = f"\n{patient_id},{first_name},{surname},{age},{ph_number},{post_code},{symptoms}"
        with open("patients.txt", "a") as file:
            file.write(line_text)
        patients.append(new_patient);
        print("Patient Registered!")

    def update_doctor(self, doctors, index):
        print('Choose the field to be updated:')
        print(' 1 First name')
        print(' 2 Surname')
        print(' 3 Speciality')
        op = int(input('Input: '))

        if op == 1:
            new_first_name = input("Enter new first name: ")
            doctors[index].set_first_name(new_first_name)
        elif op == 2:
            new_surname = input("Enter new surname: ")
            doctors[index].set_surname(new_surname)
        elif op == 3:
            new_speciality = input("Enter new speciality: ")
            doctors[index].set_speciality(new_speciality)

    def delete_doctor(self, doctors):
        print("-----Delete Doctor-----")
        print('ID |          Full Name           |  Speciality')
        self.view(doctors)

        try:
            index = int(input('Enter the ID of the doctor to be deleted: ')) - 1
            if self.find_index(index, doctors):
                doctors.pop(index)
                print("Doctor deleted successfully.")
                return True
            print("Doctor not found. Please enter a valid ID.")
        except IndexError:
            print('The ID entered is incorrect.')
        return False

    def handle_registration(self, doctors, patients):
        print("1 - Register Doctor")
        print("2 - Register Patient")
        reg_option = int(input("Option: "))
        if reg_option == 1:
            self.register_doctor(doctors)
        elif reg_option == 2:
            self.register_patient(patients)

    def doctor_management(self, doctors, patients):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """
        print("-----Doctor Management-----")
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input('Input your choice: ')

        if op == '1':
            print("-----Register-----")
            self.handle_registration(doctors, patients)
        elif op == '2':
            print("-----List of Doctors-----")
            print('ID |          Full name           |  Speciality')
            self.view(doctors)
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    if self.find_index(index, doctors):
                        self.update_doctor(doctors, index)
                        break
                    print("Doctor not found")
                except ValueError:
                    print('The ID entered is incorrect')
        elif op == '4':
            while not self.delete_doctor(doctors):
                continue
        else:
            print('Invalid operation chosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)


    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:

                # link the patients to the doctor and vice versa
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        patient_index = input('Please enter the patient ID: ')


        try:
            
            patient_index = int(patient_index) - 1
            discharge_patients.append(patients[patient_index])
            patients.pop(patient_index)
            print("Patient has been discharged sucessfully.")

        except IndexError:
            print("Enter correct ID.")


    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode')
        self.view(discharged_patients)


    def update_credentials(self, line_number: int, new_value: str):
        """Updates the specified line in the credentials file."""
        file_path = R"login.txt"

        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()

            if line_number < len(lines):
                lines[line_number] = new_value.strip() + '\n'
            else:
                print("Error: Line number out of range.")
                return

            with open(file_path, 'w') as f:
                f.writelines(lines)

            print("Update successful.")
        except FileNotFoundError:
            print("Error: Credentials file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        try:
            op = int(input('Input: '))

            if op == 1:
                new_username = input("Enter new admin username: ")
                self.update_credentials(0, new_username)

            elif op == 2:
                password = input('Enter the new password: ')
                # Validate the password
                confirm_password = input('Enter the new password again: ')
                if password == confirm_password:
                    self.update_credentials(1, password)  # Pass the password directly
                else:
                    print("Passwords do not match.")


            elif op == 3:
                new_address = input("Enter new admin address: ")
                self.update_credentials(2, new_address)

            else:
                print("Enter the correct field to be updated.")

        except ValueError:
            print("Invalid input. Choose correct field.")


    def group_patients_by_family(self, patients):
        families = {}

        for patient in patients:
            if patient.get_surname() not in families:
                families[patient.get_surname()] = []  # Initialize the family list
            families[patient.get_surname()].append(patient)

        for family, members in families.items():
            print(f"Family: {family}")
            for member in members:
                print(f"{member}")


    def get_patient_index(self, patients):
        patient_index = input('Please enter the patient ID: ')
        try:
            patient_index = int(patient_index) - 1
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return None
            return patient_index
        except ValueError:
            print('The id entered is incorrect')
            return None

    def get_doctor_index(self, doctors):
        while True:
            try:
                index = int(input('Enter the ID of the doctor: ')) - 1
                if self.find_index(index, doctors):
                    return index
                print("Doctor not found")
            except ValueError:
                print('The ID entered is incorrect')

    def validate_datetime(self):
        while True:
            date = input("Enter Date (YYYY-MM-DD): ")
            time = input("Enter Time (HH:MM): ")
            if len(date) == 10 and date[4] == '-' and date[7] == '-' and len(time) == 5 and time[2] == ':':
                return date, time
            print("Invalid format! Please use YYYY-MM-DD for date and HH:MM for time.")

    def schedule_appointment(self, doctors, patients):
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = self.get_patient_index(patients)
        if patient_index is None:
            return

        print("-----Doctors-----")
        self.view(doctors)
        doctor_index = self.get_doctor_index(doctors)

        date, time = self.validate_datetime()
        doctors[doctor_index].set_appointments(date, time)
        print(f"Patient {patients[patient_index].full_name()} has Appointment scheduled for Doctor {doctors[doctor_index].full_name()} on {date} at {time}.")

    def view_appointment_history(self, doctors):
        for doctor in doctors:
            appointments = doctor.get_appointments()
            if not appointments:
                print(f"No appointments scheduled for Dr. {doctor.full_name()}")
                continue
            
            print(f"Appointments for Dr. {doctor.full_name()} ({doctor.get_speciality()}):")
            for date, time in appointments.items():
                for times in time:
                    print(f"Date: {date} | Time: {times}")

    def appointment(self, doctors, patients):
        print(' 1 - Schedule appointment')
        print(' 2 - View Appointment History of Doctors')
        
        try:
            op = input('Input your choice: ')
            if op == '1':
                self.schedule_appointment(doctors, patients)
            elif op == '2':
                self.view_appointment_history(doctors)
        except ValueError:
            print('The choice entered is incorrect.')


    def relocate_doctor_to_patient(self, patients, doctors):

        print("-----Relocate-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode | Symptoms | Doctor\' Id: ')
        self.view(patients)
        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        current_doctor = patients[patient_index].get_doctor()

        print("-----Doctors Select-----")

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:

                # If the patient already has a doctor, remove them from the previous doctor's list
                if current_doctor:
                    for doc in doctors:
                        if doc.full_name() == current_doctor:
                            doc.remove_patient(patients[patient_index])  # Decrease count
                            break
                # link the patients to the doctor and vice versa
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                print('The patient is now relocated to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def management_report(self, doctors, patients):
        print('Choose the operation:')
        print(' 1 - Total number of doctors in the system')
        print(' 2 - Total number of patients per doctor')
        print(' 3 - Total number of appointments per month per doctor')
        print(' 4 - Total number of patients based on the illness type')

        op = int(input("Enter choice: "))

        if op == 1:
            print(f"Total number of doctors in the system: {len(doctors)}")

        elif op == 2:
            for doctor in doctors:
                num_patients = doctor.get_num_patients()
                print(f"Dr. {doctor.full_name()} has {num_patients} patients.")

        elif op == 3:
            print("\n----- Appointments Per Month -----")
            for doctor in doctors:
                print(f"\n{doctor.full_name()}'s Appointments Per Month:")

                appointments_per_month = {}

                for date in doctor.get_appointments():
                    month_year = date[:7]

                    if month_year in appointments_per_month:
                        appointments_per_month[month_year] += len(doctor.get_appointments()[date])
                    else:
                        appointments_per_month[month_year] = len(doctor.get_appointments()[date])

                if appointments_per_month:
                    for month, count in sorted(appointments_per_month.items()):
                        print(f" {month}: {count} appointments")
                else:
                    print("No appointments scheduled.")

        elif op == 4:
            pass

        else:
            print("Invalid choice.")
