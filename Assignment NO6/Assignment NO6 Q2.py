fruits = ["apple", "banana", "mango", "orange", "grape"]

print("First Item:", fruits[0])
print("Third Item:", fruits[2])
print("Last Item:", fruits[-1])
print("Second Last Item:", fruits[-2])

index = int(input("Enter an index: "))

if 0 <= index < len(fruits):
    print("Item at index", index, ":", fruits[index])
else:
    print("Invalid Index")