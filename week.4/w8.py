n = int(input("Enter number of terms: "))

total = 0.0
fact = 1

for i in range(1, n + 1):
    fact = fact * i      # calculate i!
    total = total + (i / fact)

print("Sum of the series =", total)