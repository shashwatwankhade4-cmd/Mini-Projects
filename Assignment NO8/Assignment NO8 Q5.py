s = {100, 200, 300, 400, 500}

removed = s.pop()  # Removes and returns a random element from the set
print("Popped element:", removed)

print("Set after pop:", s)

s.clear()

print("After clear:", s)

# remove(x):
# Removes x. Error if x does not exist.

# discard(x):
# Removes x if present. No error if missing.

# pop():
# Removes and returns a random element.