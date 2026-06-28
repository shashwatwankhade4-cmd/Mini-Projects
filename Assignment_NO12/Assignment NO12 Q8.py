class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)

    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])
        print()


employees = {}

for i in range(3):
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    employees[emp_id] = Employee(emp_id, name, department, salary)

print("\nEmployee Details\n")

for emp in employees.values():
    emp.show_details()