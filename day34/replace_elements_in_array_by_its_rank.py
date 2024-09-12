def replace_with_ranks(arr):
    # Sort the array and keep track of the original indices
    sorted_arr = sorted(range(len(arr)), key=lambda x: arr[x])

    # Create a rank array with the same length as the input array
    ranks = [0] * len(arr)

    # Assign ranks based on the sorted order
    for rank, index in enumerate(sorted_arr, start=1):
        ranks[index] = rank

    return ranks

# Example usage:
arr = [40, 10, 30, 20]
ranked_arr = replace_with_ranks(arr)
print(ranked_arr)
