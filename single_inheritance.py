class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("Name:", self.name)

class student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display_student(self):
        self.display_person()
        print("Roll No:", self.roll_no)

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

s = student(name, roll_no)

s.display_student()