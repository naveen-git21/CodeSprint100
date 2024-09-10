def isSubset(arr1, arr2):
    # Loop through every element in arr1 and check if it exists in arr2
    for elem in arr1:
        if elem not in arr2:
            return False
    return True

# Driver code
arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4, 5]

if isSubset(arr1, arr2):
    print("arr1 is a subset of arr2")
else:
    print("arr1 is not a subset of arr2")
