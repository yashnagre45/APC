import salary

basic = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))
deduction = float(input("Enter deductions: "))

gross = salary.gross_salary(basic, hra, da)
net = salary.net_salary(basic, hra, da, deduction)

print("Gross Salary:", gross)
print("Net Salary:", net)