# simple_swap.py
# description: a simple example of performing a Python 'swap' of two numbers
# author: pcostjr
# created: 9.29.2025
# last-update: 9.30.2025

# import libraries
import random

# generate a list of 10 random integers from 1 to 100
numbers = [random.randint(1, 100) for i in range(10)]

# print the list
print(numbers)

# for half the length of the list
for i in range(len(numbers) // 2):
    # j will run in reverse, relative to i
    j = len(numbers) - i - 1
    # swap the numbers at each index with each other
    numbers[i], numbers[j] = numbers[j], numbers[i]

# print the list
print(numbers)
