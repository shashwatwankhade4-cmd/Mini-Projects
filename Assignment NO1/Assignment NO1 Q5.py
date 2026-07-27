name = input("Enter your name: ")

birth_year = int(input("Enter your birth year: "))

# Current year is assumed to be 2026
current_year = 2026

age = current_year - birth_year

print(f"Hello {name}!")
print(f"Your age is {age} years.")

# We convert input to int because input() returns a string.
# Mathematical calculations cannot be performed on strings.