# Taking input from user

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

# BMI formula
bmi = weight / (height ** 2)

# Rounded to 2 decimal places
print("Your BMI is:", round(bmi, 2))