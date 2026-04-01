# Function to find factorial
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def is_krishnamurthy(n):
    temp = n
    s = 0

    while temp > 0:
        digit = temp % 10
        s += fact(digit)
        temp //= 10

    return s == n

num = int(input("Enter number: "))

if is_krishnamurthy(num):
    print("Krishnamurthy Number")
else:
    print("Not Krishnamurthy Number")