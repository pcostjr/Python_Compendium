# 01_bubble_sort.py
# description: A simple bubblesort program
# author: pcostjr
# created: 09.18.2024
# last update: 10.01.2025

# import random library for list generation
import random

# generate a list of 10 random numbers from -100 to 100
number_list = [random.randint(-100, 100) for i in range(1000)]
print(f"Initial Values = {number_list}")

outer_pass = 0
inner_pass = 0


def bubble_sort(values):
    # perform the bubblesort
    for i in range(len(values) - 1):
        # outer_pass += 1
        # assume the final value in each pass is sorted
        for j in range(len(values) -i - 1):
            # inner_pass += 1
            # perform the swap using a temp variable
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                # temp = values[j]
                # values[j] = values[j+1]
                # values[j+1] = temp
    # return values

bubble_sort(number_list)
print(f"Sorted Values = {number_list}")
print(f"Outer passes: {outer_pass} | Inner passes: {inner_pass}")

