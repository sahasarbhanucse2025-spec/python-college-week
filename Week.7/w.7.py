n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    x = int(input("Input element: "))
    lst.append(x)

# store last element
last = lst[-1]
# print(last)
# # shift elements to the right
for i in range(n-1, 0, -1):
    lst[i] = lst[i-1]

# # place last element at first index
lst[0] = last

print("Rotated list:", lst)