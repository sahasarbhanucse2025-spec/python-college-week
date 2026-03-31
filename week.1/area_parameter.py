# Program to calculate area and perimeter of different polygons

print("Choose a shape:")
print("1. Triangle")
print("2. Rectangle")
print("3. Circle")

choice = int(input("Enter your choice (1/2/3): "))

# Triangle
if choice == 1:
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    height = float(input("Enter height of the triangle: "))
                        
    # Area of triangle
    area = 0.5 * b * height
    
    # Perimeter of triangle
    perimeter = a + b + c
    
    print("Area of Triangle:", area)
    print("Perimeter of Triangle:", perimeter)

# Rectangle
elif choice == 2:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    
    area = length * width
    perimeter = 2 * (length + width)
    
    print("Area of Rectangle:", area)
    print("Perimeter of Rectangle:", perimeter)

# Circle
elif choice == 3:
    radius = float(input("Enter the radius: "))
    
    area = 3.14159 ** radius
    perimeter = 2 * 3.14159 * radius   # Circumference
    
    print("Area of Circle:", area)
    print("Perimeter (Circumference) of Circle:", perimeter)

else:
    print("Invalid choice!")
    