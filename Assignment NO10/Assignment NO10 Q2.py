class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print("Title :", self.title)
        print("Author:", self.author)
        print("Price :", self.price)


book1 = Book("Python Basics", "John", 450)
book2 = Book("AI Fundamentals", "Alice", 650)

book1.show_details()
print()
book2.show_details()