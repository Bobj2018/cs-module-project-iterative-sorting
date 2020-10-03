
def linear_search(arr, target):

    index = 0
    while index != len(arr):
        if arr[index] == target:
            return index
        else:
             index += 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):


    # initialize start and end
    start = 0
    end = len(arr) - 1

    while end >= start:
        # Find the middle
        middle = (start + end) // 2
        # Compare middle to target
        if target == arr[middle]:
            return middle

        if target > arr[middle]:
            start = middle + 1

        if target < arr[middle]:
            end = middle - 1

    return -1  # not found
