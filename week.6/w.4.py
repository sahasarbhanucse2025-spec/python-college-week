# Program to count different characters using list

text = input("Enter a string: ")

upper_list = []
lower_list = []
digit_list = []
special_list = []

for ch in text:
    if ch.isupper():
        upper_list.append(ch)
    elif ch.islower():
        lower_list.append(ch)
    elif ch.isdigit():
        digit_list.append(ch)
    else:
        special_list.append(ch)   # space and special characters

print("Uppercase letters:", len(upper_list))
print("Lowercase letters:", len(lower_list))
print("Digits:", len(digit_list))
print("Whitespace & special characters:", len(special_list))