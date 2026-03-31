n = int(input("Enter N: "))

# Print top dot
print(" " * (n - 1) + ".")

# Print middle part
for i in range(1, n - 1):
    print(" " * (n - i - 1) + "/" + " " * (2 * i - 1) + "\\")

# Print base
if n > 1:
    print("/" + "_" * (2 * n - 3) + "\\")

