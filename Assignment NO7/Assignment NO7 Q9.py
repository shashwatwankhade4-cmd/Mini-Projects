coordinates = (10, 20)

# Tuples are immutable

try:
    coordinates[0] = 50
except TypeError as e:
    print("Error:", e)

try:
    coordinates.append(30)
except AttributeError as e:
    print("Error:", e)

# Correct way:
temp = list(coordinates)

temp[0] = 50
temp.append(30)

coordinates = tuple(temp)

print("Modified tuple:", coordinates)