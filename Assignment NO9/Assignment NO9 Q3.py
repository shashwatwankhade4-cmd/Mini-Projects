person = {
    "name": "Priya",
    "age": 21,
    "profession": "Engineer"
}

# a) get()
print("Age:", person.get("age"))
print("Salary:", person.get("salary", "Not Available"))  # Using default value for non-existent key

# b) keys()
print("\nKeys:")
print(person.keys())

# c) values()
print("\nValues:")
print(person.values())

# d) items()
print("\nItems:")
print(person.items())