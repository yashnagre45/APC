import recursive_utils

n = int(input("Enter a non-negative integer: "))

print("Factorial:", recursive_utils.factorial(n))

print("Fibonacci Series:")
for i in range(n):
    print(recursive_utils.fibonacci(i), end=" ")

print("\nSum of Digits:", recursive_utils.sum_digits(n))
print("Binary:", recursive_utils.binary(n))