# Program to print multiplication table up to N terms

# num = int(input("Enter the number: "))
# n = int(input("Enter number of terms: "))

# for i in range(1, n + 1):
#     print(num, "x", i, "=", num * i)

















n = int(input("Enter the number of terms: "))

a = 2   # first term
r = 3   # common ratio

print("Geometric Sequence:")

for i in range(n):
    print(a, end=" ")
    a = a * r