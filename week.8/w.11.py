# Function to check palindrome
def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return original == reverse


# Main program
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Palindrome numbers are:")

for i in range(start, end + 1):
    if is_palindrome(i):
        print(i)        