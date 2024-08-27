def print_parallelogram(rows, cols):
    print()
    
    for i in range(rows):
        # Print spaces before stars
        print(" " * i, end="")
        # Print stars for each row
        print("* " * cols)
        
    print()

# Example usage
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print_parallelogram(rows, cols)
