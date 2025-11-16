# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Draw the square pattern
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
