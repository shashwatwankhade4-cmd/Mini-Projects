import math
import random

history = {}

def arithmetic():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter (+,-,*,/): ")

        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid Operator"

    except Exception as e:
        return e


def scientific():
    try:
        num = float(input("Enter number: "))
        print("1. Square Root")
        print("2. Factorial")
        print("3. Power")

        choice = input("Choice: ")

        if choice == "1":
            return math.sqrt(num)

        elif choice == "2":
            return math.factorial(int(num))

        elif choice == "3":
            power = float(input("Enter power: "))
            return math.pow(num, power)

        else:
            return "Invalid Choice"

    except Exception as e:
        return e


while True:

    print("\nSMART CALCULATOR")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Generate Random Numbers")
    print("4. Store Result")
    print("5. View History")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        result = arithmetic()
        print("Result:", result)

    elif choice == "2":
        result = scientific()
        print("Result:", result)

    elif choice == "3":
        nums = [random.randint(1, 100) for i in range(5)]
        print(nums)

    elif choice == "4":
        key = input("Enter timestamp/string key: ")
        history[key] = result
        print("Stored Successfully.")

    elif choice == "5":
        print(history)

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")