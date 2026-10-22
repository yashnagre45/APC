inventory = {
    "Pen": 20,
    "Book": 15,
    "Pencil": 30
}


def add_product(name, quantity):
    inventory[name] = quantity


def update_quantity(name, quantity):
    if name in inventory:
        inventory[name] = quantity
        print("Quantity updated")
    else:
        print("Product not found")


def remove_soldout():
    for name in list(inventory.keys()):
        if inventory[name] == 0:
            del inventory[name]


print("Initial Inventory:", inventory)

add_product("Eraser", 10)
update_quantity("Book", 25)
update_quantity("Pen", 0)
remove_soldout()

print("Updated Inventory:", inventory)
print("Product with highest stock:", max(inventory, key=inventory.get))
print("Total unique products:", len(inventory))