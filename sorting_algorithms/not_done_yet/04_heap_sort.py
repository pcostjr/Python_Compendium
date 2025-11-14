# 04_heap_sort.py
# description: A simple heap sort function. Heap Sort is an optimized version of selection sort.
# author: pcostjr
# created: 10.29.2025
# last update: 11.14.2025
import random

number_list = [random.randint(-100, 100) for i in range(10)]


# helper method: heapify subtree with root i
def heapify(arr, n, i):
    # use root as the initial max value
    max_val = i

    # left child index
    left = 2*i + 1

    # right child index
    right = 2*i + 2

    # if a child is greater than current max
    # change the max value
    if left < n and arr[left] > arr[max_val]:
        max_val = left

    if right < n and arr[right] > arr[max_val]:
        max_val = right

    if max_val != i:
        arr[i], arr[max_val] = arr[max_val], arr[i]

        # recursively heapify the subtree
        heapify(arr, n, max_val)

# actual heapsort
def heap_sort(values):
    val_len = len(values)

    # generate the heap
    for i in range(val_len // 2 -1, -1, -1):
        heapify(values, i, val_len)

    # generate the max heap, sorting the array
    for i in range(val_len - 1, 0, -1):
        values[0], values[i] = values[i], values[0]

        heapify(values, 0, i)

    return values
