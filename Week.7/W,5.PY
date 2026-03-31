n=int(input("Enter the num of elements in the list :- "))

lst=[]
for i in range(n):
    x=int(input("Enter the elements: "))
    lst.append(x)

largest = lst[0]

for num in lst:
    if num > largest:
        largest = num
print(f"The largest num is :{largest}")

    