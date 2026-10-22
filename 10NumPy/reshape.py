import numpy as np

arr = np.arange(1, 13)

print("Original Array:", arr)
print("2 x 6:\n", arr.reshape(2, 6))
print("3 x 4:\n", arr.reshape(3, 4))
print("4 x 3:\n", arr.reshape(4, 3))