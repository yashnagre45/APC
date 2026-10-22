import pandas as pd

data = """Name,Marks
Amit,85
Rahul,90
Priya,78
Sneha,92
"""

with open(r"E:\College\SEM V\APC\10NumPy\marks.csv", "w") as file:
    file.write(data)

df = pd.read_csv(r"E:\College\SEM V\APC\10NumPy\marks.csv")

print("Pandas Series:")
print(df["Marks"])