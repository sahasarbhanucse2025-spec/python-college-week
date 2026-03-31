# Program to exchange first and last character using list

text = input("Enter a string: ")

# Convert string into list
char_list = list(text)

# Check if string is not empty
if len(char_list) > 1:
    # Swap first and last character
    char_list[0], char_list[-1] = char_list[-1], char_list[0]

# Convert list back to string
new_string = "".join(char_list)

print("New string:", new_string)