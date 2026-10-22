def check_balance(balance):
    return balance


def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        return balance