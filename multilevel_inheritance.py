class Person:
    def person_info(self):
        print("Person: Person: Rahul")

class Employee(Person):
    def employee_info(self):
        print("Employee ID: 101")

class Manager(Employee):
    def manager_info(self):
        print("Department: IT")

m = Manager()

m.person_info()
m.employee_info()
m.manager_info()