students = {
    "s1": {"name": "Rahul", "age": 20, "marks": 88},
    "s2": {"name": "Sneha", "age": 21, "marks": 95}
}

# First student details
print("First Student:")
print(students["s1"])

# Second student marks
print("\nSecond Student Marks:")
print(students["s2"]["marks"])

# Add math marks
students["s1"]["math"] = 90

print("\nUpdated Dictionary:")
print(students)