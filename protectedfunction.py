class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def _display_personal_details(self):
        print("Name:", self.__name)
        print("Age:", self.__age)

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self._employee_id = employee_id
        self._salary = salary

    def _display_employee_details(self):
        self._display_personal_details()
        print("Employee ID:", self._employee_id)
        print("Salary:", self._salary)

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self._department = department

    def _display_manager_details(self):
        self._display_employee_details()
        print("Department:", self._department)

    def show_details(self):
        self._display_manager_details()

name = input("Enter manager name:")
age = int(input("Enter age:"))
employee_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))
department = input("Enter department: ")

m = Manager(name, age, employee_id, salary, department)

print("\nManager Details:")
m.show_details()