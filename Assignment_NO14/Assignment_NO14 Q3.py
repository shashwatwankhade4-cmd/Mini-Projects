import numpy as np

matrix = np.random.randint(20, 81, (4,5))

print(matrix)

print("Minimum:", matrix.min())
print("Maximum:", matrix.max())

print("Sum:", matrix.sum())
print("Mean:", matrix.mean())
print("Standard Deviation:", matrix.std())

print("Row-wise Sum:", matrix.sum(axis=1))
print("Column-wise Sum:", matrix.sum(axis=0))