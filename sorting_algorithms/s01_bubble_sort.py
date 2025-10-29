# s01_bubble_sort.py
# description: A simple bubble sort function
# author: pcostjr
# created: 09.18.2024
# last update: 10.29.2025

def bubble_sort(values):
    s_actions = 0
    s_loops = 0
    # perform the bubblesort
    for i in range(len(values) - 1):
        s_loops += 1
        # assume the final value in each pass is sorted
        for j in range(len(values) - i - 1):
            s_loops += 1
            # perform the swap using a temp variable
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                s_actions += 1
    return values, s_actions, s_loops

# traditional swap methods, for use for reference in class
# temp = values[j]
# values[j] = values[j+1]
# values[j+1] = temp
