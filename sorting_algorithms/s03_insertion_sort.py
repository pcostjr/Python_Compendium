# s03_insertion_sort.py
# description: A simple insertion sort function
# author: pcostjr
# created: 09.18.2024
# last update: 10.29.2025

def insertion_sort(values):
    s_actions = 0
    s_loops = 0
    for i in range(1, len(values)):
        s_loops += 1
        # establish the current value we're positioning
        key = values[i]
        j = i-1
        # from the point before i to the beginning of the list, backwards
        while j >= 0 and key < values[j]:
            s_loops += 1
            # move values out of the way
            values[j+1] = values[j]
            j -= 1
        # store key in the 'opening' we just made
        values[j + 1] = key
        s_actions += 1
    return values, s_actions, s_loops

