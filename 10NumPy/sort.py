import numpy as np

arr = np.array([40, 10, 50, 20, 30])

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("Original Array:", arr)
print("Ascending Order:", ascending)
print("Descending Order:", descending)