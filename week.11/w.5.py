import pandas as pd

students = {
    "Name": [],
    "Age": [],
    "Grade": []
}

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    
    name = input("Name: ")
    age = int(input("Age: "))
    grade = input("Grade: ")
    
    students["Name"].append(name)
    students["Age"].append(age)
    students["Grade"].append(grade)

# Create DataFrame
df = pd.DataFrame(students)

print("\nStudent DataFrame:")
print(df)




