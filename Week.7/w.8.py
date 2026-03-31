# number of students
n = int(input("Enter number of students: "))

students = {}

# input roll and name
for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter student name: ")
    students[roll] = name

# a) Display all records
print("\nStudent Records:")
for roll, name in students.items():
    print(roll, ":", name)

# b) Add new student
roll = int(input("\nEnter new roll number: "))
name = input("Enter new student name: ")
students[roll] = name

print("Dictionary after adding new student:")
print(students)

# c) Delete student record
roll = int(input("\nEnter roll number to delete: "))
if roll in students:
    del students[roll]
    print("Record deleted.")
else:
    print("Roll number not found.")

print("Dictionary after deletion:")
print(students)

# d) Modify existing student name
roll = int(input("\nEnter roll number to modify name: "))
if roll in students:
    name = input("Enter new name: ")
    students[roll] = name
    print("Record updated.")
else:
    print("Roll number not found.")

print("Final dictionary:")
print(students)