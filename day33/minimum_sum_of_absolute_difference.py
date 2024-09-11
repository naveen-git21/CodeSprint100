def min_sum_absolute_diff(arr):
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Find the median
    n = len(arr)
    if n % 2 == 1:
        median = arr[n // 2]  # For odd length
    else:
        median = arr[n // 2 - 1]  # For even length, you can choose either middle element
    
    # Step 3: Calculate the sum of absolute differences from the median
    min_sum_diff = sum(abs(x - median) for x in arr)
    
    return min_sum_diff

# Example usage
arr = [1, 3, 5, 9]
result = min_sum_absolute_diff(arr)
print(f"Minimum sum of absolute differences: {result}")
