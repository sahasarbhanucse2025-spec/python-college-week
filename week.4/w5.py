# Input: number of terms
N = int(input("Enter the number of terms: "))

# Initialize the first factorial
fact = 1

# Loop to generate factorial series
for i in range(1, N + 1):
    fact *= i
    print(fact, end=" ")
                                                                              