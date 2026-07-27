class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


s1 = Student("Shashwat", 97)
s2 = Student("Aditya", 32)
s3 = Student("Prem", 40)

students = [s1, s2, s3]

for s in students:
    print("Name:", s.name)
    print("Marks:", s.marks)
    print("Grade:", s.calculate_grade())
    print()