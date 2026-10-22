import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("Total Sum:", np.sum(arr))

print("Layer-wise Sum:")
print(np.sum(arr, axis=(1, 2)))

print("Row-wise Sum:")
print(np.sum(arr, axis=2))

print("Column-wise Sum:")
print(np.sum(arr, axis=1))