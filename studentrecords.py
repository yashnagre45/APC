file = open("students.txt", "w")

file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")

file.close()

file = open("students.txt", "r")

records = []

for line in file:
    data = line.strip().split(",")
    records.append(data)

file.close()

print("Student Records:")
for record in records:
    print(record[0], "-", record[1], "-", record[2])

highest = records[0]

for record in records:
    if int(record[2]) > int(highest[2]):
        highest = record

print("\nHighest Marks:")
print(highest[1], highest[2])

total = 0

for record in records:
    total = total + int(record[2])

average = total / len(records)

print("\nAverage Marks:", average)
print("\nStudents scoring more than 80:")

for record in records:
    if int(record[2]) > 80:
        print(record[0], record[1], record[2])