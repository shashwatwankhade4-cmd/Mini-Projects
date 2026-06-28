# ==========================================
# LIBRARY MANAGEMENT SYSTEM
# ==========================================

library = {}


# Add Book
def add_book():

    isbn = input("Enter ISBN Number: ")

    if isbn in library:
        print("Book already exists.")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    library[isbn] = {
        "title": title,
        "author": author,
        "available": True,
        "borrower": ""
    }

    print("Book Added Successfully.")


# View All Books
def view_catalog():

    if len(library) == 0:
        print("No Books Available.")
        return

    print("\n========== LIBRARY CATALOG ==========")

    for isbn, book in library.items():

        print("ISBN      :", isbn)
        print("Title     :", book["title"])
        print("Author    :", book["author"])

        if book["available"]:
            print("Status    : Available")
        else:
            print("Status    : Issued")
            print("Borrower  :", book["borrower"])

        print("-------------------------------------")
        # Issue Book
def issue_book():

    isbn = input("Enter ISBN Number: ")

    if isbn not in library:
        print("Book Not Found.")
        return

    if library[isbn]["available"] == False:
        print("Book Already Issued.")
        return

    borrower = input("Enter Borrower Name: ")

    library[isbn]["available"] = False
    library[isbn]["borrower"] = borrower

    print("Book Issued Successfully.")


# Return Book
def return_book():

    isbn = input("Enter ISBN Number: ")

    if isbn not in library:
        print("Book Not Found.")
        return

    if library[isbn]["available"]:
        print("Book is already available.")
        return

    library[isbn]["available"] = True
    library[isbn]["borrower"] = ""

    print("Book Returned Successfully.")


# Search Book
def search_book():

    keyword = input("Enter Book Title or Author: ")

    found = False

    for isbn, book in library.items():

        if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():

            print("\nBook Found")
            print("ISBN :", isbn)
            print("Title :", book["title"])
            print("Author :", book["author"])

            if book["available"]:
                print("Status : Available")
            else:
                print("Status : Issued")

            found = True

    if not found:
        print("No Book Found.")
        # Menu
def show_menu():

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View Catalog")
    print("6. Exit")


# Main Program
def main():

    while True:

        show_menu()

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            issue_book()

        elif choice == "3":
            return_book()

        elif choice == "4":
            search_book()

        elif choice == "5":
            view_catalog()

        elif choice == "6":
            print("Thank You for Using Library Management System")
            break

        else:
            print("Invalid Choice.")


if __name__ == "__main__":
    main()