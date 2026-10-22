import re

phone = input("Enter mobile number: ")

pattern = r'^[6-9][0-9]{9}$'

if re.match(pattern, phone):
    print("Valid mobile number")
else:
    print("Invalid mobile number")