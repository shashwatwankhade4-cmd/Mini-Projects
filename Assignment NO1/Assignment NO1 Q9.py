# Taking student details

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

mark1 = float(input("Enter marks for Science: "))
mark2 = float(input("Enter marks for Maths: "))
mark3 = float(input("Enter marks for Social Studies: "))

# Calculations
total_marks = mark1 + mark2 + mark3
percentage = (total_marks / 300) * 100

# Displaying profile
print("\n----- STUDENT PROFILE -----")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Marks:")
print("Science:", mark1)
print("Maths:", mark2)
print("Social Studies:", mark3)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")