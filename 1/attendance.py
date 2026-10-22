attendance = {
    "Amit": 90,
    "Priya": 65,
    "Rahul": 80,
    "Sneha": 70
}

present_students = {"Amit", "Rahul"}

print("Attendance Records:")

for name, percentage in attendance.items():
    print(name, ":", percentage, "%")

print("Students present today:", present_students)

print("Students with attendance below 75%:")
for name, percentage in attendance.items():
    if percentage < 75:
        print(name)