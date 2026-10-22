def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def calculate_total_amount(principal, rate, time):
    interest = calculate_simple_interest(principal, rate, time)
    return principal + interest