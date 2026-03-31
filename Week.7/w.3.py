# take string input from user
text = input("Enter a sentence: ")

# split sentence into words
words = text.split()

# create empty dictionary
freq = {}

# count frequency
for w in words:
    if w in freq:
        freq[w] = freq[w] + 1
    else:
        freq[w] = 1

# # print result
print("Word Frequency:")
for key, value in freq.items():
    print(key, ":", value)

