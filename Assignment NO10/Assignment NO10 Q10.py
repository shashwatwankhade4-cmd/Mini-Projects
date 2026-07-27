class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print("Book issued successfully.")
        else:
            print("Book is already issued.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print("Book returned successfully.")
        else:
            print("Book is already available.")

    def show_info(self):
        print("Title :", self.title)
        print("Author:", self.author)
        print("Status:", self.status)
        print()


library = []

while True:
    print("\nLibrary Menu")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Show All Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter author: ")
        library.append(Book(title, author))

    elif choice == "2":
        title = input("Enter title to issue: ")
        found = False
        for book in library:
            if book.title.lower() == title.lower():
                book.issue_book()
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "3":
        title = input("Enter title to return: ")
        found = False
        for book in library:
            if book.title.lower() == title.lower():
                book.return_book()
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "4":
        if len(library) == 0:
            print("No books in library.")
        else:
            for book in library:
                book.show_info()

    elif choice == "5":
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice.")