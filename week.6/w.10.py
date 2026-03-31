password = input("Enter your password: ")

valid = True

# Condition 1
if len(password) < 8:
    print("Password must be at least 8 characters long")
    valid = False

# Condition 2
has_upper = False
for ch in password:
    if ch.isupper():
        has_upper = True

if not has_upper:
    print("Password must contain at least one uppercase letter")
    valid = False


# Condition 3
has_lower = False
for ch in password:
    if ch.islower():
        has_lower = True

if not has_lower:
    print("Password must contain at least one lowercase letter")
    valid = False


# Condition 4
has_digit = False
for ch in password:
    if ch.isdigit():
        has_digit = True

if not has_digit:
    print("Password must contain at least one numeric digit")
    valid = False


# Final result
if valid:
    print("Password valid")








