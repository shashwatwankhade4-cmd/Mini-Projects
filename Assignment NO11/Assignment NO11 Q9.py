try:
    # Convert user input to integer
    num = int(input("Enter a number: "))

    # Divide 100 by the entered number
    result = 100 / num
    print("Result:", result)

except ValueError:
    # Handles invalid integer input
    print("Please enter a valid number.")

except ZeroDivisionError:
    # Handles division by zero
    print("Division by zero is not allowed.")

except Exception:
    # Handles any other unexpected errors
    print("Some error occurred.")