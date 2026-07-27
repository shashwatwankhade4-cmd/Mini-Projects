# a) Empty dictionary - two ways

dict1 = {}
dict2 = dict()

print("dict1 =", dict1, type(dict1))
print("dict2 =", dict2, type(dict2))

# b) Dictionary with string keys

student_info = {
    "name": "Shashwat",
    "city": "Paratwada",
    "course": "AIML"
}

print("\nString Key Dictionary:", student_info)
print(type(student_info))

# c) Dictionary with integer keys

marks = {
    1: 85,
    2: 90,
    3: 78
}

print("\nInteger Key Dictionary:", marks)
print(type(marks))

# d) Mixed data type dictionary

mixed = {
    "name": "Rahul",
    "age": 20,
    "percentage": 88.5
}

print("\nMixed Dictionary:", mixed)
print(type(mixed))