import numpy as np

# Take input
n = int(input("Enter number of random values (N): "))

# Create random array
arr = np.random.rand(n)

print("\nRandom Array:")
print(arr)

# Mean, Median, Std   
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

# Extra: using arange + reshape (just for practice) #
# arr1 = np.arange(1, 5).reshape(2, 2)
# print("\nExample (arange + reshape):")
# print(arr1)
