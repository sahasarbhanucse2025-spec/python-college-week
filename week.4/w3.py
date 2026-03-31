# Print the series: 1, 3, 7, 13, 21, 31, ...

n = int(input("Enter number of terms: "))

term = 1
even = 2

for i in range(n):
    print(term, end=" ")
    term = term + even
    even = even + 2