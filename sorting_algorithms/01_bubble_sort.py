# 01_bubble_sort.py
# description: A simple bubblesort program
# author: pcostjr
# created: 09.18.2024
# last update: 09.18.2024

# import random library for list generation
import random

# generate a list of 10 random numbers from -100 to 100
values = [random.randint(-100, 100) for i in range(1000)]
print(f"Initial Values = {values}")

# perform the bubblesort
for i in range(len(values) - 1):
    # assume the final value in each pass is sorted
    for j in range(len(values) - i - 1):
        # perform the swap using a temp variable
        if values[j] > values[j+1]:
            temp = values[j]
            values[j] = values[j+1]
            values[j+1] = temp

print(f"Sorted Values = {values}")

