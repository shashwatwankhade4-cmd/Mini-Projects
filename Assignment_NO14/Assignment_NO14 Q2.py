import numpy as np

arr = np.random.randint(1, 51, 20)

print("Array:", arr)

print("Minimum:", arr.min())
print("Index of Minimum:", arr.argmin())

print("Maximum:", arr.max())
print("Index of Maximum:", arr.argmax())

print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Standard Deviation:", arr.std())