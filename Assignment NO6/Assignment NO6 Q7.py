scores = [85, 92, 78, 92, 65, 92, 88]

print("First index of 92:", scores.index(92))
print("Count of 92:", scores.count(92))

num = int(input("Enter a number: "))

if num in scores:
    print("Index:", scores.index(num))
    print("Count:", scores.count(num))
else:
    print("Number not found")