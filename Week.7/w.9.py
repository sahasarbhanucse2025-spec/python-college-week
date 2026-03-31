d = {"EVEN": [], "ODD": []}

for i in range(6):
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        d["EVEN"].append(num)
    else:
        d["ODD"].append(num)

print("Dictionary is:", d)