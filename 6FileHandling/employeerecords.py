file = open("employees.txt", "w")
file.write("101,Amit,IT,50000\n")
file.write("102,Priya,HR,60000\n")
file.write("103,Rahul,Sales,45000\n")
file.close()


def display_employees():
    file = open("employees.txt", "r")

    for line in file:
        print(line.strip())

    file.close()


def highest_paid():
    file = open("employees.txt", "r")
    employees = []

    for line in file:
        emp_id, name, department, salary = line.strip().split(",")
        employees.append((emp_id, name, department, int(salary)))

    file.close()

    highest = max(employees, key=lambda e: e[3])
    print("Highest Paid Employee:", highest[1], highest[3])


def average_salary():
    file = open("employees.txt", "r")
    salaries = []

    for line in file:
        data = line.strip().split(",")
        salaries.append(int(data[3]))

    file.close()

    print("Average Salary:", sum(salaries) / len(salaries))


def above_salary(amount):
    file = open("employees.txt", "r")

    print("Employees earning above", amount)

    for line in file:
        data = line.strip().split(",")

        if int(data[3]) > amount:
            print(data[1], data[3])

    file.close()


display_employees()
highest_paid()
average_salary()
above_salary(50000)