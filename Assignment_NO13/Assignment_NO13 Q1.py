import numpy as np

# a) 1D array
arr1 = np.array([10, 20, 30, 40, 50])

# b) 2D array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("1D Array:")
print(arr1)
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)

print("\n2D Array:")
print(arr2)
print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)