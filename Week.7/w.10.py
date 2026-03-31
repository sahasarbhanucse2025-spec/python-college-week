sentence = input("Enter a sentence: ")

words = sentence.split()

d = {}

for w in words:
    length = len(w)
    d[length] = w

print("Dictionary is:")
print(d)
