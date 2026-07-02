import numpy as np

arr = np.array([[10,20,30,40],
                [50,60,70,80],
                [90,100,110,120]])

print("Array:")
print(arr)

print("First Row:")
print(arr[0])

print("Last Column:")
print(arr[:,3])

print("Center 2x2 Matrix:")
print(arr[1:3,1:3])

print("Even Numbers:")
print(arr[arr % 2 == 0])