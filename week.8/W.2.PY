# Source and destination file
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

# Open source file
f1 = open(source, "r")

# Read content and convert to lowercase
data = f1.read().lower()

f1.close()

# Write into destination file
f2 = open(destination, "w")
f2.write(data)
f2.close()

print("File copied with lowercase conversion!")