keys = ["name", "age", "city"]

person = dict.fromkeys(keys, None)

for key in keys:
    person[key] = input(f"Enter {key}: ")

print("\nDictionary:")
print(person)

search_key = input("Enter key to search: ")

if search_key in person:
    print("Key exists.")
else:
    print("Key does not exist.")