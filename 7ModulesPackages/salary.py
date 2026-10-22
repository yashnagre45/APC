def gross_salary(basic, hra, da):
    return basic + hra + da


def deductions(gross, amount):
    return gross - amount


def net_salary(basic, hra, da, deduction):
    gross = gross_salary(basic, hra, da)
    return gross - deduction