"""
PrinterClass    obj1        print_data()    send_data()
NetworkClass    obj2        send_data()     send_data()
DisplayClass    obj3        show_data()     send_data()
FileClass       obj4        save_data()     send_data()

lst = [obj1, obj2, obj3, obj4]
for obj in lst:
    obj.send_data()
"""


class Person:
    def __init__(self, name, age):
        self.__name = name.lower()
        self.__age = age

    def get_name(self):
        return self.__name.capitalize()

    def set_name(self, name):
        if name is not None:
            self.__name = name

    def get_age(self):
        return self.__age

    def display_info(self):
        print("Имя:", self.get_name(), "\tВозраст:", self.__age)


class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def display_info(self):
        super().display_info()
        print("Компания:", self.company)


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def display_info(self):
        print("Студент", self.get_name(), " учится в ВУЗе:", self.university)


people = [Person('Tome', 23), Student('Bob', 20, 'Harvard'), Employee('Sam', 35, 'Google')]

for obj in people:
    obj.display_info()
    print('-' * 30)
