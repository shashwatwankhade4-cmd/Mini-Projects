numbers = set()

print("Enter 6 numbers:")
for i in range(6):
    num = int(input())
    numbers.add(num)

# Add two more numbers
numbers.add(int(input("Enter first extra number: ")))
numbers.add(int(input("Enter second extra number: ")))

# Remove one number safely
numbers.discard(int(input("Enter number to discard: ")))

print("Final Set:", numbers)
print("Length:", len(numbers))