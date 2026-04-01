# Recursive function for HCF
def hcf(a, b):
    if b == 0:
        return a
    return hcf(b, a % b)

# LCM function
def lcm(a, b):
    return (a * b) // hcf(a, b)

# Input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("HCF =", hcf(x, y))
print("LCM =", lcm(x, y))


