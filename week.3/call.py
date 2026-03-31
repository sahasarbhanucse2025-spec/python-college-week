# Input number of calls
calls = int(input("Enter number of calls: "))

bill = 200  # Minimum charge for up to 100 calls

# Calculate bill based on call slabs
if calls <= 100:
    bill = 200

elif calls <= 150:
    bill = 200 + (calls - 100) * 0.60

elif calls <= 200:
    bill = 200 + (50 * 0.60) + (calls - 150) * 0.50

else:
    bill = 200 + (50 * 0.60) + (50 * 0.50) + (calls - 200) * 0.40

# Add 18% tax
tax = bill * 0.18
total_bill = bill + tax

# Display result
print("Basic bill amount: Rs.", round(bill, 2))  
print("Tax (18%): Rs.", round(tax, 2))
print("Total telephone bill: Rs.", round(total_bill, 2))                    

