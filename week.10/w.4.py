import numpy as np

# Take size
n = int(input("Enter size of square matrix (N): "))

# Create matrix using arange + reshape
arr = np.arange(1, n*n + 1).reshape(n, n)

print("\nMatrix:")
print(arr)

# Determinant
det = np.linalg.det(arr)
print("\nDeterminant:", det)

# Inverse
if det != 0:
    print("\nInverse:")
    print(np.linalg.inv(arr))
else:
    print("\nInverse not possible (Determinant = 0)")