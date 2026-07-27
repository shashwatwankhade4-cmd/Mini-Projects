def get_number():
    return int(input("Enter a number (0 to quit): "))

def is_even(num):
    return num % 2 == 0

def power(base, exp=2):
    return base ** exp

def show_result(num):
    if is_even(num):
        print("The number is Even")
    else:
        print("The number is Odd")

    print("Square =", power(num))

while True:
    number = get_number()

    if number == 0:
        print("Program Ended.")
        break

    show_result(number)
    print("-" * 20)