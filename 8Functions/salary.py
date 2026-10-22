def gross_salary(basic, hra, da):
    return basic + hra + da


basic = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))

gross = gross_salary(basic, hra, da)

print("Gross Salary: Rs.", gross)