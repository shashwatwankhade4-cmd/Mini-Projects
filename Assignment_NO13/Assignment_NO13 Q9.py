import numpy as np

arr = np.random.randint(1, 51, 20)

matrix = arr.reshape(4,5)

print("Original Array:")
print(arr)

print("\n4x5 Matrix:")
print(matrix)

print("\nSum:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Standard Deviation:", np.std(matrix))

print("\nMaximum Value in Each Row:")
print(np.max(matrix, axis=1))