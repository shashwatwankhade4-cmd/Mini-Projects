import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])

# Element-wise multiplication
print("Element-wise Multiplication:")
print(A * B)

# Matrix multiplication
print("Matrix Multiplication:")
print(A @ B)

# Difference:
# * performs multiplication between corresponding elements.
# @ performs actual matrix multiplication (dot product).