import numpy as np

# Create array of 15 random integers (0 to 100)
arr = np.random.randint(0, 100, 15)

print("Original Array:")
print(arr)

# Sort array in ascending order
sorted_arr = np.sort(arr)

print("\nSorted Array (Ascending):")
print(sorted_arr)

# Find index of minimum and maximum in sorted array
min_index = np.argmin(sorted_arr)
max_index = np.argmax(sorted_arr)

print("\nIndex of Minimum Element:", min_index)
print("Index of Maximum Element:", max_index)
