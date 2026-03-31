import math

# Take input from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
D = b**2 - 4*a*c

# Check nature of roots
if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are real and distinct")
    print("Root 1:", root1)
    print("Root 2:", root2)

elif D == 0:
    root = -b / (2*a)
    print("Roots are real and equal")
    print("Root:", root)

else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-D) / (2*a)
    print("Roots are complex")
    print(f"Root 1: {real_part} + {imaginary_part} i")
    print(f"Root 2: {real_part} - {imaginary_part} i")
