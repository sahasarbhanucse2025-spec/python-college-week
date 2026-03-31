import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit"],
    "Marks": [85, 90, 88]
})

# Mean
mean_value = df["Marks"].mean()

# Standard Deviation
std_value = df["Marks"].std()

print("Mean:", mean_value)
print("Standard Deviation:", std_value)