num = int(input("Enter a number: "))

if num in range(1, 51):
    print("Number is present in range(1, 51)")
else:
    print("Number is NOT present in range(1, 51)")

if num in range(10, 100, 5):
    print("Number is present in range(10, 100, 5)")
else:
    print("Number is NOT present in range(10, 100, 5)")