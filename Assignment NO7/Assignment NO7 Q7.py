grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')

print("Count of A:", grades.count('A'))
print("Count of B:", grades.count('B'))

grade = input("Enter a grade: ").upper()
print(f"Count of {grade}: {grades.count(grade)}")