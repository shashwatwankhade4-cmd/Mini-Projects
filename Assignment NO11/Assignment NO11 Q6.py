try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result =", result)

except ValueError:
    print("Invalid input. Please enter numbers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Division performed successfully!")

finally:
    print("Thank you for using the program.")