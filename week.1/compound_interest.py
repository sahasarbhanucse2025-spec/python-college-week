# Compound Interest Calculator

# Taking input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

# Calculating amount
amount = principal * (1 + rate / 100) ** time 

# Calculating compound interest
compound_interest = amount - principal

# Displaying the result
print("The Compound Interest is:", compound_interest)
print("The Total Amount is:", amount)
