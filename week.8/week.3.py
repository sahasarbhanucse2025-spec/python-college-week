# Number of lines
n = int(input("Enter number of lines: "))

file = open("fibonacci.txt", "w")

a, b = 1, 1

for i in range(1, n + 1):
    x, y = 1, 1
    line = ""

    for j in range(i):
        line += str(x)
        if j != i - 1:
            line += "-"
        x, y = y, x + y

    file.write(line + "\n")

file.close()

print("Fibonacci file created!")













n= int(input("NUM"))
FILE =open("Fabinocci.txt","w")
a,b=1,1
for i in range(1,n+1):
    x,y=1,1
    line=""

    for j in range(i):
        line = line+str(x)
        if j != i - 1:
            line = "-"
        x,y=y,x+y
    file.write(line+"\n")  
file.close()             