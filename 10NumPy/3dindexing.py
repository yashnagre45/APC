import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[-1, -1, -1])
print("Element [0,1,2]:", arr[0, 1, 2])
print("Element [1,2,3]:", arr[1, 2, 3])