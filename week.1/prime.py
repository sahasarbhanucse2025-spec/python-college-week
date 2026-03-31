# Take range input from user
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers in the given range are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)








# import math

# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))

# s = (a + b + c) / 2
# triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
# triangle_perimeter = a + b + c

# print("Triangle Area =", triangle_area)
# print("Triangle Perimeter =", triangle_perimeter)
