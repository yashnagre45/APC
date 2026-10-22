import numpy as np

arr = np.array([10, 60, 30, 80, 45, 90, 20])

print("Original Array:", arr)

arr[arr > 50] = 0

print("Modified Array:", arr)