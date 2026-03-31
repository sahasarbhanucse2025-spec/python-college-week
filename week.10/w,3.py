import numpy as np

# Take input
m = int(input("Enter number of rows (M): "))
n = int(input("Enter number of columns (N): "))

# Create array using arange and reshape
arr = np.arange(1, m*n + 1).reshape(m, n)

print("\nOriginal Array:")
print(arr)

# Transpose
print("\nTranspose:")
print(arr.T)

# Reshape (example: reverse shape)
print("\nReshaped Array:")
print(arr.reshape(n, m))