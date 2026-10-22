class BankAccount:
    count = 1000

    def __init__(self, account_holder):
        BankAccount.count += 1
        self.account_holder = account_holder
        self.account_number = BankAccount.count
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful")
        else:
            print("Transfer failed")


a1 = BankAccount("Amit")
a2 = BankAccount("Rahul")

a1.deposit(5000)
a1.withdraw(1000)
a1.transfer(1500, a2)

print("\nAccount 1 Details:")
a1.display_balance()

print("\nAccount 2 Details:")
a2.display_balance()