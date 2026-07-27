# Student 1
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

# Packing
student1 = name, roll, m1, m2, m3

print("\nComplete Record:")
print(student1)

# Unpacking
name, roll, m1, m2, m3 = student1

print("\nStudent Details")
print("Name:", name)
print("Roll Number:", roll)
print("Mark 1:", m1)
print("Mark 2:", m2)
print("Mark 3:", m3)

# count() method
search_mark = int(input("\nEnter mark to search: "))
print("Occurrences:", student1.count(search_mark))

# Second student
student2 = ("Aditya", 17, 85, 88, 91)
# Nested tuple
students = (student1, student2)

print("\nAll Student Records:")
print(students)

# Accessing values
print("\nFirst student's name:", students[0][0])
print("Second student's roll number:", students[1][1])
print("Second student's first mark:", students[1][2])