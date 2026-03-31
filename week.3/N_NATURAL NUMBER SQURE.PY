# Program to find sum of squares of first N natural numbers

n = int(input("Enter the value of N: "))
sum_sq = 0

for i in range(1, n + 1):
    sum_sq = sum_sq + i * i
                                                              
print("Sum of squares:", sum_sq)
                                                                              