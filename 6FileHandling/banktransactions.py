file = open("transactions.txt", "w")
file.write("Deposit,5000\n")
file.write("Withdraw,1000\n")
file.write("Deposit,2000\n")
file.write("Withdraw,500\n")
file.close()

file = open("transactions.txt", "r")

deposits = 0
withdrawals = 0
transactions = []

for line in file:
    transaction, amount = line.strip().split(",")
    amount = int(amount)

    transactions.append(amount)

    if transaction == "Deposit":
        deposits += amount
    elif transaction == "Withdraw":
        withdrawals += amount

file.close()

print("Total Deposits:", deposits)
print("Total Withdrawals:", withdrawals)
print("Final Balance:", deposits - withdrawals)
print("Largest Transaction:", max(transactions))