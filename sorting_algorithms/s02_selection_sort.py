# s02_selection_sort.py
# description: A simple selection sort function
# author: pcostjr
# created: 10.29.2025
# last update: 10.29.2025

def selection_sort(values):
    s_actions = 0
    s_loops = 0
    # perform the bubblesort
    for i in range(len(values) - 1):
        s_loops += 1
        # store a minimum value
        minimum = i
        # find the true minimum from the remaining list
        for j in range(i + 1, len(values)):
            s_loops += 1
            if values[j] < values[minimum]:
                minimum = j
            # perform the swap with the assumed minimum
        values[i], values[minimum] = values[minimum], values[i]
        s_actions += 1
    return values, s_actions, s_loops

