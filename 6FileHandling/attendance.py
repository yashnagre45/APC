file = open("attendance.txt", "w")
file.write("Amit,80,100\n")
file.write("Priya,65,100\n")
file.write("Rahul,90,100\n")
file.write("Sneha,70,100\n")
file.close()

file = open("attendance.txt", "r")

print("Attendance Records:")
print("Students below 75% attendance:")

for line in file:
    name, attended, total = line.strip().split(",")

    percentage = int(attended) / int(total) * 100

    print(name, ":", percentage, "%")

    if percentage < 75:
        print(name, "has attendance below 75%")

file.close()