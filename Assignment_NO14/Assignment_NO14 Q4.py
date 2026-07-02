import numpy as np

arr = np.arange(1,25)

a = arr.reshape(4,6)
b = arr.reshape(3,8)
c = arr.reshape(2,3,4)

print(a)
print("Shape:", a.shape)

print(b)
print("Shape:", b.shape)

print(c)
print("Shape:", c.shape)