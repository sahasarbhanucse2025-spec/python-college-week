import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit"],
    "Age": [20, 19, 21],
    "Marks": [85, 90, 88]
})

print(df)

# 1. Display one column
print("Single column (Name):")
print(df["Name"])

# 2. Display multiple columns
print("\nMultiple columns (Name, Marks):")
print(df[["Name", "Marks"]])

# 3. Dot method
print("\nUsing dot method (Age):")
print(df.Age)