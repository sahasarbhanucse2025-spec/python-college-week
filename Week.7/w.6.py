n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    x = int(input("Input element: "))
    lst.append(x)

print("Alternate elements of the list are:")

for i in range(0, n, 2):
    print(lst[i],end=" ")

