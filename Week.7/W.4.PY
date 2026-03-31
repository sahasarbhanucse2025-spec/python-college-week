# take number of elements
n = int(input("Enter number of elements: "))

lst = []

# input list elements
for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

# number to search
num = int(input("Enter the number to find: "))

# find indices
indices = []

for i in range(len(lst)):
    if lst[i] == num:
        indices.append(i)

print("Indices where the number occurs:", indices)