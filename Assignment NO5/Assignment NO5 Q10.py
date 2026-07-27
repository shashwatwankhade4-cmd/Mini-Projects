# String Analyzer

str = input("Enter a string: ")

# 1. Length

print("Length:", len(str))

# 2. First half and second half
mid = len(str) // 2

print("First Half:", str[:mid])
print("Second Half:", str[mid:])

# 3. Check for 'python' (case insensitive)
if "python" in str.lower():
    print("'python' is present in the string.")
else:
    print("'python' is not present in the string.")

# 4. Positive and negative indices
print("\nCharacter Indices:")

for i in range(len(str)):
    negative_index = i - len(str)
    print(
        f"Character: {str[i]}, "
        f"Positive Index: {i}, "
        f"Negative Index: {negative_index}"
    )

# 5. Reverse string
print("\nReverse String:", str[7::-1])