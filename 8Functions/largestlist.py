def largest(numbers):
    big = numbers[0]

    for n in numbers:
        if n > big:
            big = n

    return big


numbers = [10, 25, 8, 40, 15]

print("List:", numbers)
print("Largest element:", largest(numbers))