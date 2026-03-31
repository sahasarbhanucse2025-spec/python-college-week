rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()   # new line after each row