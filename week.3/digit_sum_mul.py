num = int(input("Enter a three digit number: "))

sum_digit = 0
product_digit = 1

while num > 0:
    digit = num % 10
    sum_digit += digit
    product_digit *= digit
    num = num // 10

print("The sum of digits of the given number:", sum_digit)
print("The product of digits of the given number:", product_digit)

