# ==========================================
# PERSONAL EXPENSE TRACKER
# ==========================================

expenses = []
budget = 0


# Set Monthly Budget
def set_budget():
    global budget

    while True:
        try:
            budget = float(input("Enter Monthly Budget: "))
            if budget > 0:
                break
            else:
                print("Budget must be greater than 0.")
        except ValueError:
            print("Invalid Input.")


# Add Expense
def add_expense():

    try:
        description = input("Enter Description: ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))
        date = input("Enter Date (DD-MM-YYYY): ")

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        expense = {
            "description": description,
            "category": category,
            "amount": amount,
            "date": date
        }

        expenses.append(expense)

        print("Expense Added Successfully!")

        total = 0
        for exp in expenses:
            total += exp["amount"]

        print("Current Total Expense: Rs.", total)

    except ValueError:
        print("Invalid Amount.")


# View Expenses
def view_expenses():

    if len(expenses) == 0:
        print("No Expenses Found.")
        return

    print("\n========== EXPENSE LIST ==========")

    count = 1

    for exp in expenses:

        print("Expense", count)
        print("Description :", exp["description"])
        print("Category    :", exp["category"])
        print("Amount      :", exp["amount"])
        print("Date        :", exp["date"])
        print("--------------------------------")

        count += 1
        # Category Summary
def category_summary():

    if len(expenses) == 0:
        print("No Expenses Found.")
        return

    summary = {}

    for exp in expenses:

        category = exp["category"]

        if category in summary:
            summary[category] += exp["amount"]
        else:
            summary[category] = exp["amount"]

    print("\n========== CATEGORY SUMMARY ==========")

    for category, total in summary.items():
        print(category, ":", total)


# Get Top Spending Category
def get_top_category():

    if len(expenses) == 0:
        return "None"

    summary = {}

    for exp in expenses:

        category = exp["category"]

        if category in summary:
            summary[category] += exp["amount"]
        else:
            summary[category] = exp["amount"]

    highest = 0
    top_category = ""

    for category in summary:

        if summary[category] > highest:
            highest = summary[category]
            top_category = category

    return top_category


# Budget Report
def budget_report():

    if len(expenses) == 0:
        print("No Expenses Found.")
        return

    total = 0

    for exp in expenses:
        total += exp["amount"]

    remaining = budget - total
    percent = (total / budget) * 100

    print("\n========== BUDGET REPORT ==========")
    print("Budget       :", budget)
    print("Total Spent  :", total)
    print("Remaining    :", remaining)
    print("Used         : {:.2f}%".format(percent))
    print("Top Category :", get_top_category())

    if percent >= 100:
        print("WARNING: Budget Exceeded!")

    elif percent >= 80:
        print("WARNING: You have used more than 80% of your budget.")

    else:
        print("Budget is under control.")


# Show Unique Categories
def show_categories():

    categories = set()

    for exp in expenses:
        categories.add(exp["category"])

    if len(categories) == 0:
        print("No Categories Found.")
    else:
        print("Unique Categories:")
        for category in categories:
            print(category)
            # Show Menu
def show_menu():

    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Show Unique Categories")
    print("6. Exit")


# Main Function
def main():

    set_budget()

    while True:

        show_menu()

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            budget_report()

        elif choice == "5":
            show_categories()

        elif choice == "6":
            print("Thank You for Using Personal Expense Tracker")
            break

        else:
            print("Invalid Choice. Please Try Again.")


# Program Starts Here
if __name__ == "__main__":
    main()