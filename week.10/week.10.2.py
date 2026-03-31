import numpy as np

# Take size input
n = int(input("Enter the size (N) of the 2D array: "))

# Create empty list
data = []

print("Enter the elements row-wise:")

# Take input row by row
for i in range(n):
    row = list(map(int, input().split()))
    data.append(row)

# Convert to NumPy array
arr = np.array(data)

# Display array
print("2D NumPy Array:")
print(arr)
