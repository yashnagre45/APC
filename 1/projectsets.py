project1 = {"Amit", "Priya", "Rahul", "Sneha"}
project2 = {"Rahul", "Sneha", "Rohit", "Neha"}

print("Project 1 Employees:", project1)
print("Project 2 Employees:", project2)

print("Employees in both projects:", project1.intersection(project2))
print("Employees only in Project 1:", project1.difference(project2))
print("Employees only in Project 2:", project2.difference(project1))
print("All unique employees:", project1.union(project2))