# Take file path and name from user
file_path = input("Enter file path with file name (example: C:/Users/file.txt): ")

# Open the file in write mode
file = open(file_path, "w")

# Take text input from user
text = input("Enter text to write in the file: ")

# Write text into file
file.write(text)

# Close the file
file.close()

print("File created and text written successfully.")

