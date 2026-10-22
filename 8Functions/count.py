def count_element(numbers, element):
    count = 0

    for n in numbers:
        if n == element:
            count += 1

    return count


numbers = [10, 20, 10, 30, 10, 40]

element = int(input("Enter element to count: "))

print("Occurrences:", count_element(numbers, element))