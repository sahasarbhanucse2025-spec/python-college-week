# Program to generate Fibonacci sequence

n = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
a, b = 0, 1

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

         




