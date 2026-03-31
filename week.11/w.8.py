import pandas as pd

# Step 1: Take user input
n = int(input("Enter number of students: "))

data = {"Name": [], "Age": [], "Grade": []}

for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    
    name = input("Name: ")
    age = int(input("Age: "))
    grade = input("Grade: ")
    
    data["Name"].append(name)
    data["Age"].append(age)
    data["Grade"].append(grade)

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Save to CSV
file_name = input("\nEnter file name to save (example: students.csv): ")
df.to_csv(file_name, index=False)

print("\n✅ CSV file created successfully!")

# Step 4: Load CSV file
df2 = pd.read_csv(file_name)

print("\n📊 Loaded Data:")
print(df2)

# Step 5: Extra (very useful)
print("\nFirst 5 rows:")
print(df2.head())

print("\nData Info:")
print(df2.info())

print("\nSummary:")
print(df2.describe())