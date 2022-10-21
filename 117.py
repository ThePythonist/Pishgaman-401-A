from Models import Person as Human


class Student(Human):
    def __init__(self, fname, lname, std_code, major):
        super().__init__(fname, lname)
        self.code = std_code
        self.major = major

    def entekhab_vahed(self):
        print("18 Vahed")
