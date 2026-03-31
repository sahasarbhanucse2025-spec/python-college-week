import numpy as np

# Take starting values from user
s1 = int(input("Enter starting value for first array: "))
s2 = int(input("Enter starting value for second array: "))

# Create arrays using arange + reshape
arr1 = np.arange(s1, s1 + 4).reshape(2, 2)
arr2 = np.arange(s2, s2 + 4).reshape(2, 2)

print("\nArray 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

# Element-wise operations
print("\nAddition:")
print(arr1 + arr2)

print("\nSubtraction:")
print(arr1 - arr2)

print("\nMultiplication:")
print(arr1 * arr2)

