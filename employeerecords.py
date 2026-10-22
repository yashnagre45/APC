file = open("employees.txt", "w")

file.write("101,Amit,IT,45000\n")
file.write("102,Priya,HR,52000\n")
file.write("103,Rahul,Sales,38000\n")

file.close()

file = open("employees.txt", "r")

employees = []

for line in file:
    data = line.strip().split(",")
    employees.append(data)

file.close()

print("Employee Records:")

for employee in employees:
    print(employee[0], employee[1], employee[2], employee[3])

highest = employees[0]

for employee in employees:
    if float(employee[3]) > float(highest[3]):
        highest = employee

print("\nHighest Paid Employee:")
print(highest[1], highest[3])

total = 0

for employee in employees:
    total = total + float(employee[3])

average = total / len(employees)

print("\nAverage Salary:", average)

salary = float(input("\nEnter salary: "))

print("\nEmployees earning above", salary, ":")

for employee in employees:
    if float(employee[3]) > salary:
        print(employee[0], employee[1], employee[2], employee[3])