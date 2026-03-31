# # Step 1: Create a file and write text
# source_file = input("Enter source file name: ")

# file = open(source_file, "w")
# text = input("Enter text to write in the file: ")
# file.write(text)
# file.close()

# # Step 2: Read the file
# with open(source_file, "r") as f:
#     content = f.read()

# print("\nOriginal Content:")
# print(content)

# # Step 3: Convert to lowercase
# content = content.lower()

# # Step 4: Copy to another file
# destination_file = input("\nEnter destination file name: ")

# with open(destination_file, "w") as f2:
#     f2.write(content)

# print("\nFile copied successfully with lowercase letters.")





# Print 500 😘 emojis in a column

for i in range(500):
    print("😘")
    