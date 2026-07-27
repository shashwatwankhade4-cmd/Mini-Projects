try:
    num = float(input("Enter a number: "))

    result = 100 / num
    print("Result =", result)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")