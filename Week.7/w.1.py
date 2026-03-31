"""lst = []

n = int(input("How many elements in the list: "))

for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

print("Original list:", lst)

# Insert
pos = int(input("Enter position to insert: "))
elem = int(input("Enter element to insert: "))

lst.insert(pos, elem)

print("List after insertion:", lst)

# Delete
pos2 = int(input("Enter position to delete: "))

lst.pop(pos2)

print("List after deletion:", lst)"""

























lst= []

a = int(input ("Enter the number of the list :-"))
for i in range(a):
    x=int (input ("Enter the elements:"))
    lst.append(x)

print(f"The original list is {lst}")

pos=int(input("Enter the position : "))
elem=int(input("Enter the element : "))

lst.insert(pos,elem)
print(f"After entering the element  The New list: {lst}" )


pos2 = int(input("Enter position to delete: "))

lst.pop(pos2)

print("List after deletion:", lst)