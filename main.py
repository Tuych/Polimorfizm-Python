from datetime import date
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def info(self):
        animal_info = f"Меня завут {self.name}. Мой возраст {self.age}"
        return animal_info

    @abstractmethod
    def make_sound(self):  # Abstract classdan meros olgan hamma classda abstractmetod bulishi shart
        ...


class Cat(Animal):

    def info(self):
        cat_info = f"Я кот. "
        cat_info += super().info()
        return cat_info

    def make_sound(self):
        cat_sound = f"{self.name} мякайет"
        return cat_sound


class Dog(Animal):
    def info(self):
        dog_info = f"Я собака. "
        dog_info += super().info()
        return dog_info

    def make_sound(self):
        dog_sound = f"{self.name} вов вов"
        return dog_sound


cat = Cat('Moshka', 2)
dog = Dog('Reks', 4)

for animal in (cat, dog):
    print(animal.info())
    print(animal.make_sound())


class Person:
    def __init__(self, firstname, lastname, passport, birthday):
        self.firstname = firstname
        self.lastname = lastname
        self.passport = passport
        self.birthday = birthday

    def get_info(self):
        info = f"{self.firstname} {self.lastname} {self.passport} {self.birthday}"
        return info

    def get_age(self):
        today = date.today()
        return today.year - self.birthday


class Student(Person):
    def __init__(self, firstname, lastname, passport, birthday, student_id, address: object):
        super().__init__(firstname, lastname, passport, birthday)
        self.student_id = student_id
        self.address = address
        self.course = 1

    def get_course(self):
        return self.course

    def update_course(self, new_course):
        self.course = new_course

    def get_info(self):
        info = super().get_info()
        info += f"{self.student_id}, {self.address.get_address()}"
        return info


class Address:
    def __init__(self, number_house, street, region, country):
        self.number_house = number_house
        self.street = street
        self.region = region
        self.country = country

    def get_address(self):
        address = f"{self.number_house}, {self.street}, {self.region}, {self.country}"
        return address


address1 = Address('14 A', 'Alisher Navoiy', 'Sergile', 'Uzbekistan')

student = Student('Baxtiyor', 'Tuychiyev', 'AB9047484', 2000, 'W12334', address1)
person = Person('Ali', 'Valiyev', 'AB5557732', 2005)

for i in (student, person):
    print(i.get_info())

"""
POLIMORFIZM — SUPER KLASS METODLARINI QAYTA YOZISH, va siklda clasdan olingan obyectlarni 1 xil nomli metdlarini chaqirish
Polimarfizm bu xar xil classlarda 1 xil nomli metodlar buladi va biz
xar xil classlardan obyect olib ularni siklda aylantirsak 1 xil nomli metodlar
har xil classlar uchun sikl ichida ishlab beradi

Tepadagi Abstract metod va Abstracl classga etibir bering Abstract claddga metodlar yozib quyiladu va Undam meros olgan
hamma classlarda shu nomli metodlar bulishi kerakligini AbS class eslatib turadi. BU uz navbatida
classdan olgan obyectlarimizni siklga solib 1 xil metodlarni quyishda xatoliklarni kamaytiradi

"""
