import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Priya"],
    "Age": [20, 19],
    "Marks": [85, 90]
})

# Rename columns
df.rename(columns={"Name": "Student_Name", "Marks": "Score"}, inplace=True)

print(df)