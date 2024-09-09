def max_product_subarray(arr):
    # Edge case: if the array is empty, return 0
    if not arr:
        return 0
    
    # Initialize the max and min products as the first element of the array
    max_product_so_far = arr[0]
    min_product_so_far = arr[0]
    global_max_product = arr[0]
    
    # Traverse through the array, starting from the second element
    for i in range(1, len(arr)):
        current = arr[i]
        
        # Calculate the temporary max_product_so_far because we will update both max and min
        temp_max = max(current, max_product_so_far * current, min_product_so_far * current)
        
        # Update min_product_so_far using the same logic
        min_product_so_far = min(current, max_product_so_far * current, min_product_so_far * current)
        
        # Update max_product_so_far with the temporary max
        max_product_so_far = temp_max
        
        # Update the global maximum product
        global_max_product = max(global_max_product, max_product_so_far)
    
    return global_max_product

# Example usage
arr = [2, 3, -2, 4, -1,6,1]
result = max_product_subarray(arr)
print("Maximum product sub-array:", result)
