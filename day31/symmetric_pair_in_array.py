def find_symmetric_pairs(pairs):
    # Set to store unique pairs
    pair_set = set()
    
    # List to store symmetric pairs
    symmetric_pairs = []
    
    # Iterate through each pair in the array
    for pair in pairs:
        first = pair[0]
        second = pair[1]
        
        # Check if the reverse pair exists in the set
        if (second, first) in pair_set:
            # Symmetric pair found
            symmetric_pairs.append((first, second))
        else:
            # Add the current pair to the set
            pair_set.add((first, second))
    
    return symmetric_pairs

# Example usage
pairs = [(1, 2), (3, 4), (5, 6), (4, 3), (4, 7),(2,1)]
result = find_symmetric_pairs(pairs)
print("Symmetric pairs:", result)
