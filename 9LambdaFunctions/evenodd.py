check = lambda n: n % 2 == 0

num = int(input("Enter a number: "))

if check(num):
    print("Even")
else:
    print("Odd")