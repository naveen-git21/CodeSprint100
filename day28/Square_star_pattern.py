print("Square star patter")
size =int(input("Enter the number for square pattern:"))
# Define the size of the square
print()
# Outer loop for the number of rows
for i in range(size):
    # Inner loop for the number of columns
    for j in range(size):
        print("*", end="  ")
    print()  # Move to the next line after each row

print()