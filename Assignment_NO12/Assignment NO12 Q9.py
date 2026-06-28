import math

try:
    sentence = input("Enter a sentence: ")

    words = sentence.lower().split()

    unique_words = set(words)

    print("Unique Words:")
    print(sorted(unique_words))

    print("Total Unique Words:", len(unique_words))
    print("Power of 2:", math.pow(len(unique_words), 2))

except Exception as e:
    print("Error:", e)