# Keep taking positive numbers and find total

total = 0

while True:
    num = float(input("Enter a positive number: "))

    if num <= 0:
        break

    total += num

print("Total Sum =", total)