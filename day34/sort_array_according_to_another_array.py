def custom_sort(arr, order):
    # Create a dictionary to store the index of each element in the `order` array
    order_map = {value: index for index, value in enumerate(order)}

    # Sort `arr` using the custom key
    sorted_arr = sorted(arr, key=lambda x: (order_map.get(x, float('inf')), x))

    return sorted_arr

# Example usage:
arr = [5, 3, 9, 7, 1, 2, 6, 8]
order = [5, 3, 7, 1]

sorted_arr = custom_sort(arr, order)
print(sorted_arr)
