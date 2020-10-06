# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i + 1
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        while cur_index != len(arr):
            if arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index
            cur_index += 1

        # TO-DO: swap
        # Your code here
        if arr[smallest_index] < arr[i]:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    first_run = True
    swapped = False

    while swapped or first_run:
        swapped = False
        first_run = False
        for i in range(0, len(arr) - 1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    buckets = dict()

    for i in range(0, maximum):
        buckets[i] = i

    for i in arr:
        buckets[i] += 1

    sorted_arr = list()

    for i in buckets:
        while i != 0:
            sorted_arr.append(i)
            buckets[i] -= 1

    return arr
