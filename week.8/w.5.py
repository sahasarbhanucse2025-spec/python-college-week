# # Given data
# books = 36
# pens = 116
# bags = 25
# notebooks = 50

# rate_books = 200
# rate_pens = 20
# rate_bags = 300
# rate_notebooks = 120

# # Calculate total
# total = (books * rate_books) + (pens * rate_pens) + (bags * rate_bags) + (notebooks * rate_notebooks)

# # Create file
# file = open("bill_vs.txt", "w")

# # Write details
# file.write(f"Books: {books}, Rate: {rate_books}\n")
# file.write(f"Pens: {pens}, Rate: {rate_pens}\n")
# file.write(f"Bags: {bags}, Rate: {rate_bags}\n")
# file.write(f"Notebook: {notebooks}, Rate: {rate_notebooks}\n")
# file.write(f"Total Price: {total}\n")


data = {}

file = open("bill_vs.txt", "r")

for line in file:
    parts = line.strip().split(":")
    key = parts[0]
    value = parts[1].strip()
    data[key] = value

file.close()

print("Dictionary:", data)