try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Invalid input.")

finally:
    print("Execution completed.")