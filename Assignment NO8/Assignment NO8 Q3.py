colors = set()

print("Enter 5 colors:")
for i in range(5):
    color = input()
    colors.add(color)

search = input("Enter a color to search: ")

if search in colors:
    print(search, "is present in the set.")
else:
    print(search, "is not present in the set.")

if search not in colors:
    print("(Checked using not in)")