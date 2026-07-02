import numpy as np

arr = np.random.randint(1,101,(5,5))

print("Original Array:")
print(arr)

print("Diagonal Elements:")
print(np.diag(arr))

print("Elements Greater than 50:")
print(arr[arr > 50])

arr[arr < 30] = 0

print("Modified Array:")
print(arr)