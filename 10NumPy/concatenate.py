import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

horizontal = np.hstack((a, b))
vertical = np.vstack((a, b))

print("Horizontal Concatenation:")
print(horizontal)

print("Vertical Concatenation:")
print(vertical)