inventory = {}

def add_items(items):
    for item_name, quantity in items.items():
        if item_name in inventory:
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity
    print("Items added to inventory.")

def remove_item(item_name, quantity):
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            print(f"Removed {quantity} {item_name}(s) from inventory.")
        else:
            print(f"Not enough {item_name}(s) in inventory to remove {quantity}.")
    else:
        print(f"{item_name} not found in inventory.")

def update_item(item_name, new_quantity):
    if item_name in inventory:
        inventory[item_name] = new_quantity
        print(f"Updated quantity of {item_name} to {new_quantity}.")
    else:
        print(f"{item_name} not found in inventory.")

def check_item(item_name):
    if item_name in inventory:
        print(f"Quantity of {item_name}: {inventory[item_name]}")
    else:
        print(f"{item_name} not found in inventory.")

def display_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def main():
    items_to_add = {
        "Apple": 5,
        "Banana": 10,
        "Orange": 7,
        "Grapes": 15
    }
    add_items(items_to_add)

    while True:
        print("\nInventory System Menu:")
        print("1. Add item(s)")
        print("2. Remove item")
        print("3. Update item quantity")
        print("4. Check item quantity")
        print("5. Display inventory")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            if item_name in inventory:
                inventory[item_name] += quantity
            else:
                inventory[item_name] = quantity
            print(f"Added {quantity} {item_name}(s) to inventory.")
        elif choice == "2":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            remove_item(item_name, quantity)
        elif choice == "3":
            item_name = input("Enter item name: ")
            new_quantity = int(input("Enter new quantity: "))
            update_item(item_name, new_quantity)
        elif choice == "4":
            item_name = input("Enter item name: ")
            check_item(item_name)
        elif choice == "5":
            display_inventory()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    display_inventory()

if __name__ == "__main__":
    main()



