from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, speed, wheels=0):
        self.speed = speed
        self.wheels = wheels

    @abstractmethod
    def move(self):
        pass

    def showInfo(self):
        print(f"Speed {self.speed}  Wheels {self.wheels}")


class Car(Transport):
    def __init__(self, model, speed, wheels):
        super().__init__(speed, wheels)
        self.model = model

    def move(self):
        print("Car is moving ")

    def showInfo(self):
        print(f"Model : {self.model} ", end=" ")
        super().showInfo()


class Boat(Transport):

    def __init__(self, motor, speed):
        super().__init__(speed)
        self.motor = motor

    def move(self, tmp):
        return self.speed + tmp

    def showInfo(self):
        print(f"Model : {self.motor} ", end=" ")
        super().showInfo()

    def charging(self):
        print("Hello")


obj = Car("A4", 310, 21)
obj.showInfo()
obj.move()

obj1 = Boat("jz20", 200)
print("Boat boost: ", obj1.move(50))
obj1.showInfo()
obj1.charging()

from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def progress_level(self):
        pass

    def showInfo(self):
        print(f"Name {self.name}, Age {self.age}")


class Admin(User):
    def __init__(self, name, age, Id, password):
        super().__init__(name, age)
        self.Id = Id
        self.password = password

    def progress_level(self):
        print("Seniour")

    def showAdmin(self):
        self.showInfo()
        print(f"Id: {self.Id}, password: {self.password}")


class Guest(User):
    def __init__(self, name, age, hour):
        super().__init__(name, age)
        self.hour = hour

    def progress_level(self):
        print("Junior")

    def showGuest(self):
        self.showInfo()
        print(f"Hours: {self.hour}")


AdminObj = Admin("Ababa", 25, "A123", "gjgfx")
AdminObj.showAdmin()
AdminObj.progress_level()
print()

GuestObj = Guest('Boba', 19, 8)
GuestObj.showGuest()
GuestObj.progress_level()

from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl

    def progress_lvl(self):
        print(f"Name:{self.name}, lvl:{self.lvl}")


class Admin(User):

    def __init__(self, name, lvl, expirience, work):
        super().__init__(name, lvl)
        self.expirience = expirience
        self.work = work

    def progress_lvl(self):
        super().progress_lvl()
        print(f"Expirience:{self.expirience} year, work:{self.work}")


class Guest(User):

    def __init__(self, name, lvl, gadjet):
        super().__init__(name, lvl)
        self.gadjet = gadjet

    def progress_lvl(self):
        super().progress_lvl()
        print(f"Gadjet:{self.gadjet}")


admin = Admin("Maks", 'junior', 1, 'programmer')
guest = Guest("Maks", 'junior', "phone")
admin.progress_lvl()
guest.progress_lvl()

from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def progress_lvl(self):
        pass

    def display_info(self):
        print(f"імя {self.name}, вік {self.age}")


class Admin(User):
    def __init__(self, name, age, role, permissions):
        super().__init__(name, age)
        self.role = role
        self.permissions = permissions

    def progress_lvl(self):
        if self.permissions > 5:
            return "senior"
        elif self.permissions > 2:
            return "middle"
        else:
            return "junior"

    def display_info(self):
        super().display_info()
        print(f"роль {self.role}, дозволи {self.permissions}")


class Guest(User):
    def __init__(self, name, age, visit_date):
        super().__init__(name, age)
        self.visit_date = visit_date

    def progress_lvl(self):
        return "guest"

    def display_info(self):
        super().display_info()
        print(f"дата візиту {self.visit_date}")


admin = Admin(name="Артур", age=666, role="Хто я?", permissions=6)
guest = Guest(name="Васька", age=777, visit_date="2024-09-20")

admin.display_info()
print(f"ступінь {admin.progress_lvl()}\n")

guest.display_info()
print(f"ступінь {guest.progress_lvl()}")

from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @abstractmethod
    def progress_lvl(self):
        pass

    def showInfo(self):
        print(f"name {self.name}, surname {self.surname}")


class Admin(User):
    def __init__(self, name, surname, id, login):
        super().__init__(name, surname)
        self.id = id
        self.login = login

    def progress_lvl(self):
        print("senior ")

    def showInfo1(self):
        self.showInfo()
        print(f"Id {self.id}, login {self.login}")


class Guest(User):

    def __init__(self, name, surname, time):
        super().__init__(name, surname)
        self.time = time

    def progress_lvl(self):
        print("junior")

    def showInfo2(self):
        self.showInfo()
        print(f"time: {self.time}")


obj = Admin("f", "n", 1, 2255)
obj.progress_lvl()
obj.showInfo1()

obj1 = Guest("b", "f", "4h")
obj1.progress_lvl()
obj1.showInfo2()


def showInfo(self):
    print(f"name {self.name}, surname {self.surname}")


class Admin(User):
    def __init__(self, name, surname, id, login):
        super().__init__(name, surname)
        self.id = id
        self.login = login

    def progress_lvl(self):
        print("senior ")

    def showInfo1(self):
        self.showInfo()
        print(f"Id {self.id}, login {self.login}")


class Guest(User):

    def __init__(self, name, surname, time):
        super().__init__(name, surname)
        self.time = time

    def progress_lvl(self):
        print("junior")

    def showInfo2(self):
        self.showInfo()
        print(f"time: {self.time}")


obj = Admin("f", "n", 1, 2255)
obj.progress_lvl()
obj.showInfo1()

obj1 = Guest("b", "f", "4h")
obj1.progress_lvl()
obj1.showInfo2()

from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, gajet):
        self.name = name
        self.gajet = gajet

    @abstractmethod
    def progress_lvl(self):
        pass


class Admin(User):
    def __init__(self, name, gajet, work, age):
        super().__init__(name, gajet)
        self.work = work
        self.age = age

    def showAdmin(self):
        print(f'{self.name} {self.gajet} {self.work} {self.age}')

    def progress_lvl(self):
        print('junior')


class Guest(User):
    def __init__(self, name, gajet, work):
        super().__init__(name, gajet)
        self.work = work

    def showGuest(self):
        print(f'{self.name} {self.gajet} {self.work}')

    def progress_lvl(self):
        print('junior')


obj = Admin('Igor', 'IOs', 'Builder', 60)
obj1 = Guest('Vlad', 'IOs', 'Builder')
obj.showAdmin()
obj1.showGuest()
obj.progress_lvl()
obj1.progress_lvl()

"""
керування різними типами роботів, використовуючи абстрактні класи та конструктори.
Абстрактний клас Robot:
•Поля: name (ім’я робота), model (модель робота), power_level (рівень заряду).
•Метод: show_info(), який виводить інформацію про робота.
•Абстрактний метод perform_task(), який буде реалізований у похідних класах.
•Метод charge(), який збільшує рівень заряду на задану кількість (максимум 100).
Клас WorkerRobot, який успадковує Robot:
•Додаткове поле: tool (інструмент, яким користується робот).
•Реалізація методу perform_task(), який виводить інформацію про виконання завдання, використовуючи інструмент, і зменшує рівень заряду на 10 одиниць 
за кожне завдання.
Клас DefenseRobot, який успадковує Robot:
•Додаткове поле: weapon (зброя, якою користується робот).
•Реалізація методу perform_task(), який виводить інформацію про виконання захисного завдання, використовуючи зброю, і зменшує рівень заряду на 15 
одиниць за кожне завдання.
Клас ServiceRobot, який успадковує Robot:
•Додаткове поле: service_type (тип обслуговування, яке надає робот).
•Реалізація методу perform_task(), який виводить інформацію про надання послуг і зменшує рівень заряду на 5 одиниць за кожне завдання.

1. Створити об’єкти для кожного з підкласів:
•Робота-робітника з іменем Bob, моделлю X1, інструментом Wrench.
•Робота-захисника з іменем Defender, моделлю Z3, зброєю Laser.
•Робота-службовця з іменем Helper, моделлю S2, типом обслуговування Cleaning.
Кожен робот повинен виконати декілька завдань та зарядитися на певну кількість одиниць.
Викликати методи show_info() та perform_task() для кожного робота і відобрази зміну рівня заряду.

"""
