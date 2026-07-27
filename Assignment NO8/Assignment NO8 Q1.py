# a) Set with 5 integers
set1 = {10, 20, 30, 40, 50}

# b) Set with mixed data types
set2 = {100, "Python", 3.14}

# c) Empty set (correct way)
set3 = set()
# d) Set from string "hello"
set4 = set("hello")

print("Set1:", set1, type(set1))
print("Set2:", set2, type(set2))
print("Set3:", set3, type(set3))
print("Set4:", set4, type(set4))

# Sets automatically remove duplicate values.
# Example: "hello" contains two 'l' characters,
# but the set keeps only one 'l'.