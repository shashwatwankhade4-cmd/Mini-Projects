d = {"a": 1, "b": 2}

# Copy dictionary
copy_d = d.copy()

# Add key if not exists
d.setdefault("c", 3)

# Existing key
d.setdefault("a", 100)

print("Original Dictionary:")
print(d)

print("Copied Dictionary:")
print(copy_d)