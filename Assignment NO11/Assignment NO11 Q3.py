try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Division =", result)

    text = input("Enter a number as string: ")
    number = int(text)
    print("Integer =", number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input. Please enter numeric values.")