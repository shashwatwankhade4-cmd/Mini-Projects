str = input("Enter a string: ")

print("Characters with indices:")

for i in range(len(str)):
    print("Index", i, ":", str[i])

print("\nString in reverse:")

for i in range(len(str)-1, -1, -1):
    print(str[i], end="")
