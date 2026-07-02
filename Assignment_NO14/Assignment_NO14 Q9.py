import numpy as np

arr = np.random.randn(6,6)

print(arr)

print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)

print("Maximum Index:", np.unravel_index(arr.argmax(), arr.shape))
print("Minimum Index:", np.unravel_index(arr.argmin(), arr.shape))

print("Top Left 3x3 Matrix:")
print(arr[:3,:3])

arr[arr < 0] = np.abs(arr[arr < 0])

print("Modified Array:")
print(arr)

print("Mean:", arr.mean())