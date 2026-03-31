n = int(input("Enter number of rows (middle height): "))

# Upper half (including middle)
for i in range(1, n + 1):
    spaces = n - i
    nums = 2 * i - 1
    print(" " * spaces + "".join(str(x) for x in range(1, nums + 1)))

# Lower half
for i in range(n - 1, 0, -1):
    spaces = n - i
    nums = 2 * i - 1
    print(" " * spaces + "".join(str(x) for x in range(1, nums + 1)))