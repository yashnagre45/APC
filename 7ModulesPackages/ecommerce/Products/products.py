products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1000
}


def display_products():
    for name, price in products.items():
        print(name, "- Rs.", price)