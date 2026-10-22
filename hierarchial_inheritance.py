class Person:
    def person_info(self):
        print("Name: Rahul")

class Student(Person):
    def student_info(self):
        print("Roll No: 101")

class Employee(Person):
    def employee_info(self):
        print("Employee ID: 201")

s = Student()
e = Employee()

s.person_info()
s.student_info()

e.person_info()
e.employee_info()