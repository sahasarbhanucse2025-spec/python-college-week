def is_armstrong(n):
    power = len(str(n))
    temp = n
    s = 0

    while temp > 0:
        digit = temp % 10
        s += digit ** power
        temp //= 10

    return s == n

num = int(input("Enter number: "))

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")