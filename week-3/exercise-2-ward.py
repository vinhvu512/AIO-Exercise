from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


class Ward:
    def __init__(self, name):
        self._name = name
        self._people = []

    def add_person(self, person):
        self._people.append(person)

    def describe(self):
        print(f"Ward Name: {self._name}")
        for person in self._people:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self._people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self._people.sort(key=lambda x: x._yob)

    def compute_average(self):
        total = 0
        count = 0
        for person in self._people:
            if isinstance(person, Teacher):
                total += person._yob
                count += 1

        return total / count

