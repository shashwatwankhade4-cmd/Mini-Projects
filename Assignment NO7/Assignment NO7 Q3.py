colors = ('red', 'green', 'blue', 'yellow', 'purple', 'orange')

print("First element:", colors[0])
print("Third element:", colors[2])
print("Last element:", colors[-1])
print("Second last element:", colors[-2])

index = int(input("Enter index number: "))

if -len(colors) <= index < len(colors):
    print("Element:", colors[index])
else:
    print("Invalid index")