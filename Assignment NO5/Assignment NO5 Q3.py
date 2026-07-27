main_string = input("Enter main string: ")
substring = input("Enter substring: ")

if substring in main_string:
    print("Substring found!")
else:
    print("Substring not found!")

if substring not in main_string:
    print("Confirmed: Substring not present.")