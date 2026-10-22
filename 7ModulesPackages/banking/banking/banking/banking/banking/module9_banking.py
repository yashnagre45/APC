from banking import account, transaction, loan

balance = float(input("Enter initial balance: "))
amount = float(input("Enter deposit amount: "))

balance = account.deposit(balance, amount)
transaction.transaction_details(amount, "Deposit")

print("Updated Balance:", account.check_balance(balance))

withdraw_amount = float(input("Enter withdrawal amount: "))
balance = account.withdraw(balance, withdraw_amount)

transaction.transaction_details(withdraw_amount, "Withdrawal")
print("Final Balance:", account.check_balance(balance))

principal = float(input("Enter loan amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time in years: "))

interest = loan.calculate_simple_interest(principal, rate, time)
total = loan.calculate_total_amount(principal, rate, time)

print("Loan Interest:", interest)
print("Total Loan Amount:", total)