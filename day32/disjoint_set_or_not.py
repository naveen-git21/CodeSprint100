# Function to check if two sets are disjoint
def areDisjoint(set1, set2, m, n):
    # Take every element of set1 and search it in set2
    for i in range(m):
        for j in range(n):
            if set1[i] == set2[j]:
                return False  # Found a common element

    # No element of set1 is present in set2
    return True

# Driver code
set1 = [12, 34, 11, 9, 3]
set2 = [7, 2, 1, 5]
m = len(set1)
n = len(set2)

# Check if sets are disjoint and print the result
if areDisjoint(set1, set2, m, n):
    print("Yes, the sets are disjoint.")
else:
    print("No, the sets are not disjoint.")
