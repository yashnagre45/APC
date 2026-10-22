from Products import products as product_module
from Cart import cart as cart_module
from Orders import orders

product_module.display_products()

while True:
    name = input("\nEnter product name (or done): ")

    if name.lower() == "done":
        break

    if name in product_module.products:
        price = product_module.products[name]
        cart_module.add_to_cart(name, price)
    else:
        print("Product not found.")

total = cart_module.calculate_total()

print("\nCart Total: Rs.", total)
orders.place_order(total)