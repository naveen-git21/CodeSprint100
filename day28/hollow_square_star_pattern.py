print("Hollow Square star pattern")
size = int(input('Enter the size of the square:'))

# Outer loop for the number of rows
for i in range(size):
    # Inner loop for the number of columns
    for j in range(size):
        # Print stars on the border of the square
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end="  ")
        else:
            print(" ", end="  ")  # Print space for the hollow part
    print()  # Move to the next line after each row
