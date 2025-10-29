# s04_merge sort.py
# description: A simple merge sort function
# author: pcostjr
# created: 10.29.2025
# last update: 10.29.2025

# perform the merge sort
# value left = the
s_recurs = 0
s_parts = 0

def merge(values, left, right, mid):
    global s_parts
    size_l = mid - left + 1
    size_r = right - mid

    left_values = []
    right_values = []

    # copy the values into two separate arrays
    for i in range(size_l):
        left_values.append(values[left + i])
    for i in range(size_r):
        right_values.append(values[mid + i + 1])

    s_parts += 1
    l = 0
    r = 0
    v = left

    while l < size_l and r < size_r:
        if left_values[l] <= right_values[r]:
            values[v] = left_values[l]
            l += 1
        else:
            values[v] = right_values[r]
            r += 1
        v += 1

    while l < size_l:
        values[v] = left_values[l]
        l += 1
        v += 1

    while r < size_r:
        values[v] = right_values[r]
        r += 1
        v += 1

def merge_sort_helper(values, left, right):
    global s_recurs
    s_recurs += 1
    if left < right:
        mid = (left + right) // 2
        merge_sort_helper(values, left, mid)
        merge_sort_helper(values, mid + 1, right)
        merge(values, left, right, mid)

def merge_sort(values):
    global s_recurs, s_parts
    s_recurs = 0
    s_parts = 0
    merge_sort_helper(values, 0, len(values) - 1)
    return values, s_recurs, s_parts

