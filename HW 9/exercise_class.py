class People:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.__parching = False

    def who_i_am(self):
        print(f'My name is,{self.name}. I am {self.age} years old. ')


    def say_city(self):
        print("I live in ", self.city)

    def parching(self, not_parching):
        if not_parching:
            print("Parching(((.")
            self.__parching = False
        else:
            print("Hasn't Parching out yet.")

class Employee(People):

    def __init__(self,name, age, city, company, experience, salary):
        super().__init__(name, age, city)
        self.company = company
        self.experience = experience
        self.salary = salary


    def about_me(self):
        print(f'My name is,{self.city}. I am {self.age} years old .')
        print(f'I work in a - {self.company},my experience- {self.experience}.')
        print(f'In secret I get - {self.salary},only shhhh;).')



employee1 = Employee("Tanya", 37, "Minsk", "Alfa-bank", "19 years", "2500b")
employee2 = Employee("Oleg", 30, "Poland", "Google", "12 years", "5000b")
employee3 = Employee("Vika", 19, "Pinsk", "Tech Corp", "1 years", "700b")


print("Employee 1:")
employee1.who_i_am()
employee1.say_city()
employee1.parching(False)
employee1.about_me()

print("\nEmployee 2:")
employee2.who_i_am()
employee2.say_city()
employee2.parching(True)
employee2.about_me()

print("\nEmployee 3:")
employee3.who_i_am()
employee3.say_city()
employee3.parching(False)
employee3.about_me()


