# Read number of terms
N = int(input("Enter the number of terms: "))

term = 2
print("Series:")
for i in range(N):
    print(term, end=" ")
    term *= 2
    