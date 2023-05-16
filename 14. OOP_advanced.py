class Person:
    def print_info(self):
        print(f'Person: Name - {self.name}, Surname - {self.surname}, {self.place_of_birth}')

    def get_age(self, currentYear):
        return currentYear - self.year_of_birth

p1 = Person()
p1.name = "Vahe"
p1.surname = "Aghajanyan"
p1.place_of_birth = "Armenia"
p1.year_of_birth = 1999

p1.print_info()
Person.print_info(p1)
print(p1.get_age(2023))