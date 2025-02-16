from Person import Person

class Doctor(Person):
    """A class that deals with the Doctor operations"""

    def __init__(self, id, first_name, surname, speciality):
        super().__init__(id, first_name, surname)

        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        # self.__first_name = first_name
        # self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = {}


   
    def get_speciality(self) :
        #ToDo6
        return self.__speciality

    def set_speciality(self, new_speciality):
        #ToDo7
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_patients(self):
        return self.__patients

    def get_num_patients(self):
        return len(self.__patients)

    def get_appointments(self):
        return self.__appointments

    def set_appointments(self, date, time):
        if date not in self.__appointments:
            self.__appointments[date] = []  # Create a list for the date if it doesn't exist

        self.__appointments[date].append(time)

    def remove_patient(self,patient):
        if patient in self.__patients:
            self.__patients.remove(patient)

    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
