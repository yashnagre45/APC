def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter a number: "))

print("The number is", check_even_odd(num))