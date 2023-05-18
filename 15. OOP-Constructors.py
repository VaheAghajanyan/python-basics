class Person:
    def __init__(self, name, surname, place_of_birth, year_of_birth):
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        self.year_of_birth = year_of_birth

    def print_info(self):
        print(f'Person: Name - {self.name}, Surname - {self.surname}, {self.place_of_birth}')

    def get_age(self, currentYear):
        return currentYear - self.year_of_birth


p1 = Person("Vahe", "Aghajanyan", "Yerevan", 1999)
p1.print_info()