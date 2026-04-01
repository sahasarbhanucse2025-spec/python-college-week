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




