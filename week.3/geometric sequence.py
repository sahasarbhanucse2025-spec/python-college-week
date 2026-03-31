# Read number of terms
N = int(input("Enter the number of terms: "))

first_term = 2
common_ratio = 3

term = first_term

print("Geometric Sequence:")
for i in range(N):
    print(term, end=" ")
    term *= common_ratio
