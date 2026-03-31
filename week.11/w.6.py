import pandas as pd

data = []
n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    
    name =  input("Name: ")
    age = int(input("Age: "))
    grade = input("Grade: ")
    
    data.append([name, age, grade])   # list of lists

# Create DataFrame
df = pd.DataFrame(data, columns=["Name", "Age", "Grade"])

print("\nStudent DataFrame:")
print(df)