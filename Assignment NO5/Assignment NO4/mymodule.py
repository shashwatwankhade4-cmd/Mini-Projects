import math
import random

# Lambda function
square = lambda x: x * x

# Normal function using math module
def calculate_power(base, exp):
    return math.pow(base, exp)

while True:
    print("\n===== Math Utility Program =====")
    print("1. Square")
    print("2. Power")
    print("3. Random Number")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num = float(input("Enter a number: "))
        print("Square =", square(num))

    elif choice == "2":
        base = float(input("Enter base: "))
        exp = float(input("Enter exponent: "))
        print("Power =", calculate_power(base, exp))

    elif choice == "3":
        print("Random Number =", random.randint(1, 100))

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Try Again.")