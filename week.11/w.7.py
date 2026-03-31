import pandas as pd

# Take input
n = int(input("Enter number of students: "))

data = {"Name": [], "Age": [], "Grade": []}

for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    
    data["Name"].append(input("Name: "))
    data["Age"].append(int(input("Age: ")))
    data["Grade"].append(input("Grade: "))

# Create DataFrame
df = pd.DataFrame(data)
                                                                                                        
# Save to CSV
df.to_csv("students.csv", index=False)
print("\nCSV file created successfully!")

# Read CSV file
df2 = pd.read_csv("students.csv")

print("\nData from CSV file:")
print(df2)
 

 









# import pandas as pd

# Sample data
# data = {
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Age": [20, 19, 21],
#     "Grade": ["A", "B", "A"]
# }

# Create DataFrame
# df = pd.DataFrame(data)

# Save as CSV file
# df.to_csv("students.csv", index=False)

# print("CSV file created!")