"""Write a program that input a string and ask user to delete a
given word from the string."""

text = input("Enter a sentence: ")
word = input("Enter the word to delete: ")

new_text = text.replace(word, "")

print("Updated sentence:", new_text)