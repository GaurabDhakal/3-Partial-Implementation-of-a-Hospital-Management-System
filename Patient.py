from Person import Person
class Patient(Person):
    """Patient class"""

    def __init__(self, id, first_name, surname, age, mobile, postcode, symptoms, doctor=None):
        super().__init__(id,first_name, surname)
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = doctor;
        self.__id = id
        self.__symptoms = symptoms

    def full_name(self) :
        """full name is first_name and surname"""
        return f'{self.get_first_name()} {self.get_surname()}'
    def get_doctor(self) :
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        print(self.__symptoms)

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{self.__symptoms:^10}|{self.__id:^10}'
