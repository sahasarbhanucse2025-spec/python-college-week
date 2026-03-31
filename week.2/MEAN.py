import math

# Input 5 scores from the user
scores = []
for i in range(5):
    value = float(input(f"Enter score {i+1}: "))
    scores.append(value)

# Calculate Mean
mean = sum(scores) / 5

# Calculate Variance (Population)
variance = sum((x - mean) ** 2 for x in scores) / 5

# Calculate Standard Deviation
std_dev = math.sqrt(variance)

# Output the results
print("Mean of scores:", mean)
print("Standard Deviation:", std_dev)





import math

# Taking 5 scores from user
scores = []

for i in range(5):
    num = float(input("Enter score: "))
    scores.append(num)

# Calculate mean
mean = sum(scores) / 5

# Calculate standard deviation
total = 0
for x in scores:
    total = total + (x - mean) ** 2

std_dev = math.sqrt(total / 5)

# Print results
print("Mean =", mean)
print("Standard Deviation =", std_dev)
