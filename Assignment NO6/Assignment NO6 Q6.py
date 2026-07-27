items = [10, 20, 30, 20, 40, 50]

# remove() removes by value
items.remove(20)
print("After remove(20):", items)

# pop() removes by index and returns removed value
removed = items.pop(3)
print("Removed Value:", removed)
print("After pop(3):", items)

items.pop()
print("After pop():", items)

items.clear()
print("After clear():", items)