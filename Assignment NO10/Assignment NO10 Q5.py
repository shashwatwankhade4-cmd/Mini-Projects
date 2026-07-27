class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

    def give_raise(self, amount):
        self.salary += amount
        print("New Salary:", self.salary)

    def yearly_bonus(self):
        return self.salary * 0.10


emp = Employee("Shashwat", 50000)

emp.display_details()
emp.give_raise(50000)
print("Yearly Bonus:", emp.yearly_bonus())