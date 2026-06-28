# ==========================================
# INVENTORY MANAGEMENT SYSTEM
# ==========================================

inventory = {}
transactions = []


# Add Product
def add_product():

    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        print("Product ID already exists.")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")

    try:
        price = float(input("Enter Unit Price: "))
        quantity = int(input("Enter Quantity: "))
        reorder = int(input("Enter Reorder Level: "))

        inventory[product_id] = {
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "reorder": reorder
        }

        print("Product Added Successfully.")

    except ValueError:
        print("Invalid Input.")


# Stock In
def stock_in():

    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product Not Found.")
        return

    try:
        qty = int(input("Enter Quantity to Add: "))

        inventory[product_id]["quantity"] += qty

        transactions.append(
            "IN : " + product_id + " Qty : " + str(qty)
        )

        print("Stock Updated Successfully.")

    except ValueError:
        print("Invalid Quantity.")


# Stock Out
def stock_out():

    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product Not Found.")
        return

    try:
        qty = int(input("Enter Quantity to Remove: "))

        if qty > inventory[product_id]["quantity"]:
            print("Insufficient Stock.")
            return

        inventory[product_id]["quantity"] -= qty

        transactions.append(
            "OUT : " + product_id + " Qty : " + str(qty)
        )

        print("Stock Removed Successfully.")

    except ValueError:
        print("Invalid Quantity.")


# View Inventory
def view_inventory():

    if len(inventory) == 0:
        print("Inventory Empty.")
        return

    print("\n========== INVENTORY ==========")

    for pid, product in inventory.items():

        print("Product ID :", pid)
        print("Name       :", product["name"])
        print("Category   :", product["category"])
        print("Price      :", product["price"])
        print("Quantity   :", product["quantity"])
        print("Reorder    :", product["reorder"])
        print("--------------------------------")
        # Low Stock Alert
def low_stock_alert():

    found = False

    print("\n========== LOW STOCK ITEMS ==========")

    for pid, product in inventory.items():

        if product["quantity"] <= product["reorder"]:

            print("Product ID :", pid)
            print("Name       :", product["name"])
            print("Quantity   :", product["quantity"])
            print("Reorder    :", product["reorder"])
            print("--------------------------------")

            found = True

    if not found:
        print("No Low Stock Items.")


# Generate Report
def generate_report():

    if len(inventory) == 0:
        print("Inventory Empty.")
        return

    total_products = len(inventory)
    total_value = 0
    categories = set()

    for product in inventory.values():

        total_value += product["price"] * product["quantity"]
        categories.add(product["category"])

    print("\n========== INVENTORY REPORT ==========")
    print("Total Products :", total_products)
    print("Total Stock Value :", total_value)

    print("Categories :")
    for category in categories:
        print(category)

    print("\nTransaction History")

    if len(transactions) == 0:
        print("No Transactions.")
    else:
        for transaction in transactions:
            print(transaction)


# Save Inventory
def save_inventory():

    try:

        file = open("inventory.txt", "w")

        for pid, product in inventory.items():

            data = pid + "," + \
                   product["name"] + "," + \
                   product["category"] + "," + \
                   str(product["price"]) + "," + \
                   str(product["quantity"]) + "," + \
                   str(product["reorder"]) + "\n"

            file.write(data)

        file.close()

        print("Inventory Saved Successfully.")

    except:
        print("Error Saving File.")


# Load Inventory
def load_inventory():

    try:

        file = open("inventory.txt", "r")

        for line in file:

            data = line.strip().split(",")

            inventory[data[0]] = {
                "name": data[1],
                "category": data[2],
                "price": float(data[3]),
                "quantity": int(data[4]),
                "reorder": int(data[5])
            }

        file.close()

    except FileNotFoundError:
        pass
    # Show Menu
def show_menu():

    print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. View Inventory")
    print("5. Low Stock Alert")
    print("6. Generate Report")
    print("7. Save & Exit")


# Main Function
def main():

    load_inventory()

    while True:

        show_menu()

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            stock_in()

        elif choice == "3":
            stock_out()

        elif choice == "4":
            view_inventory()

        elif choice == "5":
            low_stock_alert()

        elif choice == "6":
            generate_report()

        elif choice == "7":
            save_inventory()
            print("Thank You for Using Inventory Management System")
            break

        else:
            print("Invalid Choice. Please Try Again.")


# Program Starts Here
if __name__ == "__main__":
    main()