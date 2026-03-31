import pandas as pd
import numpy as np

# Input
n = int(input("Enter number of students: "))

data = {"Name": [], "Age": [], "Marks": []}

for i in range(n):
    print("\nStudent", i+1)
    
    data["Name"].append(input("Name: "))
    
    age = input("Age (leave empty if missing): ")
    marks = input("Marks (leave empty if missing): ")
    
    data["Age"].append(float(age) if age else np.nan)
    data["Marks"].append(float(marks) if marks else np.nan)

# Create DataFrame
df = pd.DataFrame(data)

print("\nOriginal Data:")
print(df)

# Handle missing values (fill with mean)
df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nFinal Output (Missing values handled):")
print(df)