def analyze_string(s):
    if len(s) == 0:
        print("Empty string entered!")
        return

    # Length
    print("Length:", len(s))

    # Reverse
    print("Reverse:", s[::-1])

    # Count vowels
    vowels = "aeiou"
    count = 0

    for v in s.lower():
        if v in vowels:
            count += 1

    print("Number of vowels:", count)

    # Positive and Negative Index
    print("\nCharacter\tPositive Index\tNegative Index")

    for i in range(len(s)):
        print(f"{s[i]}\t\t{i}\t\t{i-len(s)}")


# User Input
text = input("Enter a string: ")
analyze_string(text)