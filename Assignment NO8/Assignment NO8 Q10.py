items = set()

while True:
    print("\n----- MENU -----")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show All Items")
    print("4. Check Item")
    print("5. Clear All Items")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item: ")
        items.add(item)
        print("Item added.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        items.discard(item)
        print("Item removed (if present).")

    elif choice == "3":
        print("Unique Items:", items)

    elif choice == "4":
        item = input("Enter item to check: ")
        if item in items:
            print("Item exists.")
        else:
            print("Item does not exist.")

    elif choice == "5":
        items.clear()
        print("All items cleared.")

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")