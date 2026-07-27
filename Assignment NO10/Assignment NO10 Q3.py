class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn.")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print("Current Balance:", self.balance)


acc = BankAccount("Shashwat", 5000)

acc.show_balance()
acc.deposit(2000)
acc.withdraw(1000)
acc.withdraw(10000)
acc.show_balance()