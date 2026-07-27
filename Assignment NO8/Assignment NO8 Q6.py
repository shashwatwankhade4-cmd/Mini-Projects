set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

copy_set = set1.copy()

set1.update(set2)

print("Original copy:", copy_set)
print("Updated set1:", set1)