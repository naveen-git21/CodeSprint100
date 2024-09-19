def rowWithMax1s(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Start from the top-right corner
    max_row_index = -1
    j = cols - 1  # Start from the last column
    
    for i in range(rows):
        # Move left while we encounter 1's in the current row
        while j >= 0 and matrix[i][j] == 1:
            j -= 1
            max_row_index = i  # Update the row index with the most 1's
    
    return max_row_index

# Example usage:
matrix = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]

result = rowWithMax1s(matrix)
print(f"Row with maximum 1's is: {result}")
