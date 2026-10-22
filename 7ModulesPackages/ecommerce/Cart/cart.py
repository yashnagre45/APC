cart = []


def add_to_cart(product, price):
    cart.append((product, price))
    print(product, "added to cart.")


def calculate_total():
    total = 0

    for product, price in cart:
        total += price

    return total