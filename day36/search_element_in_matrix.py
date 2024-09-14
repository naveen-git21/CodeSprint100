def search_element(matrix, target):
    # Iterate through each row and each element in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return (i, j)  # Return the position if the element is found
    return None  # Return None if the element is not found

# Example usage
matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]

target = 29
result = search_element(matrix, target)

if result:
    print(f"Element found at position: {result}")
else:
    print("Element not found")
