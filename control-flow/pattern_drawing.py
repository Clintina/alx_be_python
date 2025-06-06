# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Use a while loop to iterate through rows
while row < size:
    # Use a for loop to print asterisks side by side
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line
    row += 1