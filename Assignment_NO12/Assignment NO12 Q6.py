import random
import math

numbers = set()

while len(numbers) < 10:
    try:
        num = int(input("Enter number: "))
        numbers.add(num)
    except ValueError:
        print("Invalid input!")

numbers_tuple = tuple(numbers)

print("Tuple:", numbers_tuple)

try:
    random_numbers = random.sample(numbers_tuple, 3)
    print("Random Numbers:", random_numbers)

    total = sum(numbers_tuple)
    print("Square Root of Sum:", math.sqrt(total))

except Exception as e:
    print("Error:", e)