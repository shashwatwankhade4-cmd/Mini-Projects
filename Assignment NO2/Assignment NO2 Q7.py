# Weather advice program

temperature = int(input("Enter temperature: "))
is_raining = input("Is it raining? (yes/no): ").lower()

if temperature > 30:
    if is_raining == "yes":
        print("Hot and rainy, carry umbrella.")
    else:
        print("Hot day, wear light clothes.")

elif temperature < 15:
    if is_raining == "yes":
        print("Cold and rainy, wear jacket and take umbrella.")
    else:
        print("Cold day, wear warm clothes.")

else:
    print("Weather is moderate. Dress comfortably.")