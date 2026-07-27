try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result =", result)

except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

finally:
    # This block always executes whether an exception occurs or not.
    print("Program execution completed.")