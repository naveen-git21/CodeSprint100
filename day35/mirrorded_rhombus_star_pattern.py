def mirrored_rhombus(n):
    for i in range(n):
        # Print leading spaces
        print(' ' * (n - i - 1), end='')
        # Print stars with spaces between them
        print(' * ' * n)

# Example usage
n = int(input("Enter the size: "))
mirrored_rhombus(n)
