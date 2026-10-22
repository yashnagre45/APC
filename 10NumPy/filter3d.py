import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

flat = arr.flatten()

print("Original 3D Array:")
print(arr)

print("Elements Greater Than 50:")
print(flat[flat > 50])

print("Even Elements:")
print(flat[flat % 2 == 0])

print("Elements Greater Than 80:")
print(flat[flat > 80])