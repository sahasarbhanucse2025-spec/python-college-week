# Program to check palindrome using swap in list

text = input("Enter a string: ")

# convert string to list
char_list = list(text)

# create another list for reverse
rev_list = char_list.copy()

# swap to reverse the list
n = len(rev_list)

for i in range(n // 2):
    rev_list[i], rev_list[n-i-1] = rev_list[n-i-1], rev_list[i]

# convert lists back to string
original = "".join(char_list)
reversed_str = "".join(rev_list)

# check palindrome
if original == reversed_str:
    print("Palindrome")
else:
    print("Not a palindrome")

    