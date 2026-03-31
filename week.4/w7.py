N = int(input("Enter a Number:- "))
total = 0.0

for i in range(1, N + 1):
    total += (-1) ** (i + 1) / i

print(f"The sum of the series is : {total}")




N = int(input("Enter a Number:- "))

total = 0.0

for i in range(1, N + 1):
    if i % 2 == 0:
        total -= 1 / i   # even term → subtract
    else:
        total += 1 / i   # odd term → add

print(f"The sum of the series is : {total}")
