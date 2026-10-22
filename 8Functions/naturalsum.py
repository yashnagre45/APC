def natural_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


num = int(input("Enter a number: "))

print("Sum:", natural_sum(num))