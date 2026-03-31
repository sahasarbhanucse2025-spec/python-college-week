# Program to find the largest and smallest among 3 numbers

# Taking input from the user
numbers = input("Enter three numbers separated by commas: ")

# Splitting and converting to integers
a, b, c = map(float, numbers.split(','))

# Finding largest and smallest
largest = max(a, b, c)
smallest = min(a, b, c)
 
print("Largest number is:", largest)
print(f"Smallest number is: {smallest}")

















