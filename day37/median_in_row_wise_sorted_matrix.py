import bisect

def findMedian(matrix):
    r = len(matrix)
    c = len(matrix[0])

    # Initialize the minimum and maximum elements
    min_val = matrix[0][0]
    max_val = matrix[0][c-1]
    for i in range(1, r):
        min_val = min(min_val, matrix[i][0])
        max_val = max(max_val, matrix[i][c-1])

    desired = (r * c + 1) // 2

    while min_val < max_val:
        mid_val = (min_val + max_val) // 2
        place = 0

        # Find count of elements smaller than or equal to mid_val
        for i in range(r):
            place += bisect.bisect_right(matrix[i], mid_val)

        if place < desired:
            min_val = mid_val + 1
        else:
            max_val = mid_val

    return min_val

matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
print("Median is:", findMedian(matrix))
