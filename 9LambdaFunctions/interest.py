simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

print("Simple Interest:", simple_interest(p, r, t))