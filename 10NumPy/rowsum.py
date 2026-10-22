import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Matrix:")
print(arr)

print("Row Sums:", np.sum(arr, axis=1))
print("Column Sums:", np.sum(arr, axis=0))