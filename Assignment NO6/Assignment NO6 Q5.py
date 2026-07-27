cities = []

# Taking user input
city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

cities.append(city1)
cities.append(city2)

cities.append("Mumbai")
cities.append("Delhi")
cities.append("Chennai")

cities.insert(2, "Pune")

print("Final List:", cities)