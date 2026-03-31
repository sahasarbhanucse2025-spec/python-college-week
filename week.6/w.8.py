name = input("Enter your full name: ").strip()

initials = ""

initials += name[0] + ". "

for i in range(len(name)):
    if name[i] == " ":
        initials += name[i+1] + ". "

print("Initials:", initials)                   


