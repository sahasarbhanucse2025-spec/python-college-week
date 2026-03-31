# Program to calculate the sum of reciprocals from 1 to N

# Take input from the user
N = int(input("Enter a positive integer N: "))

# Initialize sum
reciprocal_sum = 0.0

# Loop to calculate the sum of reciprocals
for i in range(1, N + 1):
    reciprocal_sum += 1 / i

# Display the result
print(f"The sum of reciprocals from 1 to {N} is: {reciprocal_sum}")



