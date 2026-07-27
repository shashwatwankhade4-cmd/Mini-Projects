list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using extend()
extend_list = list1.copy()
extend_list.extend(list2)

# Using append()
append_list = list1.copy()
append_list.append(list2)

print("Using extend():", extend_list)
print("Using append():", append_list)

# extend() adds elements individually
# append() adds entire list as one element