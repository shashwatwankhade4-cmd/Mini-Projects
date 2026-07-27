data = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50
}

# popitem removes last inserted item
item1 = data.popitem()
print("Removed:", item1)

item2 = data.popitem()
print("Removed:", item2)

# clear removes all elements
data.clear()

print("After clear():")
print(data)

# Difference:
# pop(key) removes a specific key.
# popitem() removes the last inserted key-value pair.