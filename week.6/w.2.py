# Program to count vowels using list

# Take input from user
text = input("Enter a string: ")

# Create list of vowels
vowels = ['a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U']

# Create empty list to store vowels found
found = []

# Check each character
for ch in text:
    if ch in vowels:
        found.append(ch)

# Display result
print("Vowels in string:", found)
print("Number of vowels:", len(found))



























text = input ("Enter a string :- ")

vowels = ['A','E','I','O','U','a','e','i','o','u']

empty_list=[]

for ch in text:
    if ch in vowels:
        empty_list.append(ch)

print(f"The string is {empty_list} and the length is {len(empty_list)}")