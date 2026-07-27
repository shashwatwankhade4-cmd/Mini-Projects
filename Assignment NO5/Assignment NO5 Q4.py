str = input("Enter a string: ")


print("Length of string:", len(str))

# Last character using len()
print("Last character:", str[len(str) - 1])

# Middle character if length is odd
if len(str) % 2 != 0:
    middle = len(str) // 2
    print("Middle character:", str[middle])
else:
    print("Length is even, no single middle character.")

# Common mistake:
# len(str) gives total count, last index is len(str)-1