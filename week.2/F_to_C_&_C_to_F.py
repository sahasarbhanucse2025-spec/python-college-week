print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")

choice = int(input("Enter the choice: "))

result = 0

if choice in [1, 2]:
    if choice == 1 :
        C = float(input("Temperature in Celsius: "))
        result = (C * 9/5) + 32

    if choice == 2:
        F = float(input("Temperature in Fahrenheit: "))
        result = (F - 32) * 5/9

else:
    print("Invalid choice")

print(f"The result of the operation is {result}")
