# Take input and convert it to integer
num = int(input("Enter a number: "))

# Added missing colon (:)
if num > 100:
    print("Large number")

# Added missing colon (:)
elif num > 50:
    print("Medium number")

else:
    print("Small number")

# Initialize counter
count = 1

# Added missing colon (:)
while count < 10:
    print(count)

    # Corrected increment statement
    count += 1